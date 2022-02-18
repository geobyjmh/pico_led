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
    
    def pixels_show(self):
        dimmer_ar = array.array("I", [0 for _ in range(self.get_number_of_leds())])
        for i,c in enumerate(self.ar):
            r = int(((c >> 8) & 0xFF) * self.brightness)
            g = int(((c >> 16) & 0xFF) * self.brightness)
            b = int((c & 0xFF) * self.brightness)
            dimmer_ar[i] = (g<<16) + (r<<8) + b
        ws2812_pio_driver.write_to_neopixel(dimmer_ar)

    def pixels_set(self,color, i):
        self.ar[i] = (color[1]<<16) + (color[0]<<8) + color[2]

    def pixels_fill(self, color):
        for i in range(len(self.ar)):
            self.pixels_set(color, i)
     
    def wheel(self, pos):
        # Input a value 0 to 31 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 31:
            return (0, 0, 0)
        if pos < 10:
            return (31 - pos * 3, pos * 3, 0)
        if pos < 15:
            pos -= 10
            return (0, 31 - pos * 3,pos * 3)
        pos -= 15
        return (pos * 3, 0, 31 - pos * 3)
     
     
    def rainbow_cycle(self, wait):
        for j in range(256):
            for i in range(self.get_number_of_leds()):
                rc_index = (i * 256 // self.get_number_of_leds()) + j
                self.pixels_set(self.wheel(rc_index & 31), i)
            self.pixels_show()
            time.sleep(wait)