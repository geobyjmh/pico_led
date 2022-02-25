#https://github.com/geobyjmh/pico_led
import array, time
import ws2812_pio_driver
import colour
from NeoPixel import NeoPixel
from position import position

LED_ROW_COUNT = 16
LED_COL_COUNT = 10
TOTAL_LED_COUNT = LED_ROW_COUNT * LED_COL_COUNT

LED_COUNT = 5

def turn_off_all_leds():
    strip.pixels_fill(colour.BLACK)
    strip.pixels_show()
    time.sleep(0.05)
    
def init_position():
    x = position(0, LED_ROW_COUNT-1)
    y = position(0, LED_COL_COUNT-1)
    return x, y

def add_pixel_to_list(pixels, x, y):
    pixels.append([x.get_value(), y.get_value()])
    if len(pixels) > LED_COUNT:
        pixels.pop(0) 
    return pixels

def pattern1():
    print('pattern1')
    x,y = init_position()
    pixels = list()

    while(1):
        pixels = add_pixel_to_list(pixels, x, y)
        for p in pixels:
            strip.pixel_set_xy(colour.WHITE, p[0], p[1])
        strip.pixels_show()
        time.sleep(0.1)
        turn_off_all_leds()    

if __name__=='__main__':
    strip = NeoPixel()
    pattern1()
    turn_off_all_leds()
    

    
    
        





