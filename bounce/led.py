#https://github.com/geobyjmh/pico_led
import array, time
import ws2812_pio_driver
import colour
from NeoPixel import NeoPixel       

LED_ROW_COUNT = 16
LED_COL_COUNT = 10
TOTAL_LED_COUNT = LED_ROW_COUNT * LED_COL_COUNT

def turn_off_all_leds():
    strip.pixels_fill(colour.BLACK)
    strip.pixels_show()
    time.sleep(0.05)
    
  
def pattern1():
    print('pattern1')
    #for y in range(LED_COL_COUNT):
    turn_off_all_leds()
    #for x in range(LED_ROW_COUNT):
    x = 0
    xjump = 1
    
    y = 0
    yjump = 1
    
    while(1):
        strip.pixel_set_xy(colour.WHITE, x, y)
        strip.pixels_show()
        time.sleep(0.05)
        turn_off_all_leds()
        x += xjump
        if x == LED_ROW_COUNT - 1:
           xjump = -1
        if x == 0:
            xjump = 1
            
        y += yjump
        if y == LED_COL_COUNT - 1:
           yjump = -1
        if y == 0:
            yjump = 1
        
    
    

if __name__=='__main__':
    strip = NeoPixel()
    pattern1()
    turn_off_all_leds()
    

    
    
        





