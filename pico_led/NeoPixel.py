#https://github.com/geobyjmh/pico_led
import array
import time
import ws2812_pio_driver

class NeoPixel(object):
    def __init__(self,brightness=0.8):
        self.brightness = brightness
        ws2812_pio_driver.create_and_run_pio_statemachine()
        self.create_led_array()
          
    def create_led_array(self):
        self.leds = array.array("I", [0 for _ in range(self.get_number_of_leds())])
          
    def get_number_of_leds(self):
        return ws2812_pio_driver.get_number_of_leds()
    
    def __rgb_brightness(self, c, brightness):
        r = int(((c >> 8) & 0xFF) * brightness)
        g = int(((c >> 16) & 0xFF) * brightness)
        b = int((c & 0xFF) * brightness)
        adjusted_rgb = (g<<16) + (r<<8) + b
        return adjusted_rgb
    
    def __rgb_combine(self, color):
        return (color[1]<<16) + (color[0]<<8) + color[2]
        
    def pixels_show(self):
        dimmer_leds = array.array("I", [0 for _ in range(self.get_number_of_leds())])
        for i,c in enumerate(self.leds):
            dimmer_leds[i] = self.__rgb_brightness(c, self.brightness)
        ws2812_pio_driver.write_to_neopixel(dimmer_leds)

    def pixels_set(self,color, i):
        self.leds[i] = self.__rgb_combine(color)

    def pixels_fill(self, color):
        for i in range(len(self.leds)):
            self.pixels_set(color, i)
     