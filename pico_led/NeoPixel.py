#https://github.com/geobyjmh/pico_led
import array
import time
import ws2812_pio_driver

class NeoPixel(object):
    def __init__(self,brightness=0.8):
        self.brightness = brightness
        
        ws2812_pio_driver.create_and_run_pio_statemachine()

        # Display a pattern on the LEDs via an array of LED RGB values.
        self.ar = array.array("I", [0 for _ in range(self.get_number_of_leds())])
          
    ##########################################################################
    def get_number_of_leds(self):
        return ws2812_pio_driver.get_number_of_leds()
    
    def __rgb(self, c):
        r = int(((c >> 8) & 0xFF) * self.brightness)
        g = int(((c >> 16) & 0xFF) * self.brightness)
        b = int((c & 0xFF) * self.brightness)
        combined_rgb = (g<<16) + (r<<8) + b
        return combined_rgb
        
    def pixels_show(self):
        dimmer_ar = array.array("I", [0 for _ in range(self.get_number_of_leds())])
        for i,c in enumerate(self.ar):
            dimmer_ar[i] = self.__rgb(c)
        ws2812_pio_driver.write_to_neopixel(dimmer_ar)

    def pixels_set(self,color, i):
        self.ar[i] = (color[1]<<16) + (color[0]<<8) + color[2]

    def pixels_fill(self, color):
        for i in range(len(self.ar)):
            self.pixels_set(color, i)
     