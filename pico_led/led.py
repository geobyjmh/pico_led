#https://github.com/geobyjmh/pico_led
import array, time
import ws2812_pio_driver
from NeoPixel import NeoPixel       

def turn_off_all_leds():
    strip.pixels_fill(strip.BLACK)
    strip.pixels_show()
    time.sleep(0.05)
    
def pattern1():
    print("chases")

    for color in range(0,160): #从下往上显示            
        strip.color_chase(strip.COLORS[color%2], color)
        if (color+1)%16 == 0 or (color+1)%160 == 0:
            strip.pixels_show()
            time.sleep(0.05)
    
    
def pattern2():
    for color in range(159,-1,-1):             
        strip.color_chase(strip.COLORS[color%3], color)
        if color%16 ==0 or color%144 == 0:
            print((color)%15)
            strip.pixels_show()
            time.sleep(0.05)
    
def pattern3():
    for color in range(159,-1,-1):             
        strip.color_chase(strip.COLORS[color%3], color)
        if color%16 ==0 or color%144 == 0:
            print((color)%15)
            strip.pixels_show()
            time.sleep(0.05)
    
def pattern4():
    color1 = 0
    color2 = 15
    num1 = 0
    num2 = 1
    num3 = 15
    for color in range(0,160):
        print("color1:",color1)
        strip.color_chase(strip.COLORS[color%4], color1)
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
    color1 = 0
    color2 = 15
    num1 = 0
    num2 = 1
    num3 = 15
    for color in range(0,160):
        strip.color_chase(strip.COLORS[color%5], color2)
        color2 += 16
        if color2 > 159:
            num3 -=1
            if num3 < 0:
                num3=15
            color2 = num3
        print("num3:",num3)
        if  color2-1 == num3-1:
            strip.pixels_show()
            time.sleep(0.05)
        
def pattern6():
    color1 = 0
    num1 = 0
    num2 = 1       
    for color in range(0,160):
        strip.color_chase(strip.BLACK, color1)
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
    for color in range(0,160):
        strip.color_chase(strip.lattice[color], color)
    strip.pixels_show()
    time.sleep(0.5)
    
    
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
    
    
    print("rainbow")
    #todo refactor tis secition when done above
    #while(1):
    #    strip.rainbow_cycle(0.002)    





