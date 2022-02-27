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
    global strip
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

def pixel_set(pixels):
    global strip
    for p in pixels:
        strip.pixel_set_xy(colour.get_random_colour(), p[0], p[1])
    
    
def pixel_loop(x, y, pixels):
    global strip
    pixels = add_pixel_to_list(pixels, x, y)
    pixel_set(pixels)
    strip.pixels_show()
    time.sleep(0.1)
    turn_off_all_leds()
    

def pixel_pattern():
    x,y = init_position()
    pixels = list()

    while(1):
        pixel_loop(x, y, pixels)
        

def init_globals():
    global strip
    strip = NeoPixel()

def main():
    init_globals()
    pixel_pattern()
    
def main_with_exceptions():
    try:
        main()
    except:
        turn_off_all_leds()
    
if __name__=='__main__':
    main_with_exceptions()
    
     
   
    

    
    
        





