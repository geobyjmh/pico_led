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
    
def show_led_line_by_line(pixel_position):
    pixel_position_at_end_of_row = (pixel_position+1)%LED_ROW_COUNT == 0
    if pixel_position_at_end_of_row:
            strip.pixels_show()
            time.sleep(0.05)
            
def wheel(pos):
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
     
     
def rainbow_cycle(wait):
    for j in range(256):
        for i in range(TOTAL_LED_COUNT):
            rc_index = (i * 256 // TOTAL_LED_COUNT) + j
            strip.pixels_set(wheel(rc_index & 31), i)
        strip.pixels_show()
        time.sleep(wait)
       
def pattern1():
    print('pattern1')
    for color in range(0,160):            
        strip.pixels_set(colour.COLORS[color%2], color)
        show_led_line_by_line(color)
    
    
def pattern2():
    print('pattern2')
    for color in range(159,-1,-1):             
        strip.pixels_set(colour.COLORS[color%3], color)
        show_led_line_by_line(color)
    
def pattern3():
    print('pattern3')
    for color in range(159,-1,-1):             
        strip.pixels_set(colour.COLORS[color%3], color)
        show_led_line_by_line(color)
    
def pattern4():
    print('pattern4')
    color1 = 0
    num1 = 0
    num2 = 1
    for color in range(0,160):
        strip.pixels_set(colour.COLORS[color%4], color1)
        color1 += 16
        if color1 > 159:
            num1 +=1
            if num1 == 17:
                num1=0
            color1 = num1
        if  color1/num2 == 1 or num1/16 == 1 :
            num2 += 1
            if num2 >16:
                num2=2
            strip.pixels_show()
            time.sleep(0.05)
    
def pattern5():
    print('pattern5')
    color2 = 15
    num3 = 15
    for color in range(0,160):
        strip.pixels_set(colour.COLORS[color%5], color2)
        color2 += 16
        if color2 > 159:
            num3 -=1
            if num3 < 0:
                num3=15
            color2 = num3
        if  color2-1 == num3-1:
            strip.pixels_show()
            time.sleep(0.05)
        
def pattern6():
    print('pattern6')
    color1 = 0
    num1 = 0
    num2 = 1       
    for color in range(0,160):
        strip.pixels_set(colour.BLACK, color1)
        color1 += 16
        if color1 > 159:
            num1 +=1
            if num1 == 17:
                num1=0
            color1 = num1
        if  color1/num2 == 1 or num1/16 == 1 :
            num2 += 1
            if num2 >16:
                num2=2
            strip.pixels_show()
            
def pattern7():
    print('pattern7')
    for color in range(0,160):
        strip.pixels_set(colour.PATTERN_121[color], color)
    strip.pixels_show()
    time.sleep(0.5)
 
def pattern_for_ever():
     print("pattern_for_ever")
     try:
         while(1): rainbow_cycle(0.002)
     except:
         turn_off_all_leds()
     
    
if __name__=='__main__':
    strip = NeoPixel()

    pattern1()
    turn_off_all_leds()
    
    pattern2()
    turn_off_all_leds()
    
    pattern3()
    turn_off_all_leds()
    
    pattern4()
    turn_off_all_leds()
    
    pattern5()
    turn_off_all_leds()
    
    pattern6()
    turn_off_all_leds()
    
    pattern7()
    turn_off_all_leds()
    
    pattern_for_ever()
    
        





