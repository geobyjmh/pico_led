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
        
        self.BLACK = (0, 0, 0)
        self.RED = (15, 0, 0)
        self.YELLOW = (15, 15, 0)
        self.GREEN = (0, 15, 0)
        self.CYAN = (0, 15, 15)
        self.BLUE = (0, 0, 15)
        self.PURPLE = (15, 0, 15)
        self.WHITE = (15, 15, 15)
        self.COLORS = [self.RED, self.YELLOW, self.GREEN, self.CYAN, self.BLUE, self.PURPLE, self.WHITE,self.BLACK ]
        self.lattice = [self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN,
                        self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.CYAN, self.RED, self.RED, self.RED, self.RED, self.CYAN, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN,
                        self.CYAN, self.RED, self.RED, self.RED, self.CYAN, self.RED, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.RED, self.CYAN, self.RED, self.RED, self.RED, self.CYAN,
                        self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN,
                        self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN,
                        self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN,
                        self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN,
                        self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.RED, self.RED, self.RED, self.RED, self.RED, self.RED, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN,
                        self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN,
                        self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN]
        
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

    def pixels_set(self, i, color):
        self.ar[i] = (color[1]<<16) + (color[0]<<8) + color[2]

    def pixels_fill(self, color):
        for i in range(len(self.ar)):
            self.pixels_set(i, color)

    def color_chase(self, color, length):
        #for i in range(self.get_number_of_leds()):
        self.pixels_set(length, color)
            #time.sleep(wait)
#         self.pixels_show()
#         time.sleep(0.2)
     
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
                self.pixels_set(i, self.wheel(rc_index & 31))
            self.pixels_show()
            time.sleep(wait)