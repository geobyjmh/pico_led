#This code was taken from the waveshare online resource to support the WAV-20170 which can be found at  https://www.waveshare.com/wiki/Pico-RGB-LED
# Example using PIO to drive a set of WS2812 LEDs.
import array, time
from machine import Pin
import rp2

# Configure the number of WS2812 LEDs.
NUM_LEDS = 160
PIN_NUM = 6

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()
        
class NeoPixel(object):
    def __init__(self,pin=PIN_NUM,num=NUM_LEDS,brightness=0.8):
        self.pin=pin
        self.num=num
        self.brightness = brightness
        
        # Create the StateMachine with the ws2812 program, outputting on pin
        self.sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))

        # Start the StateMachine, it will wait for data on its FIFO.
        self.sm.active(1)

        # Display a pattern on the LEDs via an array of LED RGB values.
        self.ar = array.array("I", [0 for _ in range(self.num)])
        
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
    def pixels_show(self):
        dimmer_ar = array.array("I", [0 for _ in range(self.num)])
        for i,c in enumerate(self.ar):
            r = int(((c >> 8) & 0xFF) * self.brightness)
            g = int(((c >> 16) & 0xFF) * self.brightness)
            b = int((c & 0xFF) * self.brightness)
            dimmer_ar[i] = (g<<16) + (r<<8) + b
        self.sm.put(dimmer_ar, 8)

    def pixels_set(self, i, color):
        self.ar[i] = (color[1]<<16) + (color[0]<<8) + color[2]

    def pixels_fill(self, color):
        for i in range(len(self.ar)):
            self.pixels_set(i, color)

    def color_chase(self, color, length):
        #for i in range(self.num):
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
            for i in range(self.num):
                rc_index = (i * 256 // self.num) + j
                self.pixels_set(i, self.wheel(rc_index & 31))
            self.pixels_show()
            time.sleep(wait)

if __name__=='__main__':
    strip = NeoPixel()
    color1 = 0
    color2 = 15
    num1 = 0
    num2 = 1
    num3 = 15

    print("chases")


    for color in range(0,160): #从下往上显示            
        strip.color_chase(strip.COLORS[color%2], color)
        if (color+1)%16 == 0 or (color+1)%160 == 0:
            strip.pixels_show()
            time.sleep(0.05)
    strip.pixels_fill(strip.BLACK)
    strip.pixels_show()
    time.sleep(0.05)
    
    for color in range(159,-1,-1):             
        strip.color_chase(strip.COLORS[color%3], color)
        if color%16 ==0 or color%144 == 0:
            print((color)%15)
            strip.pixels_show()
            time.sleep(0.05)
    strip.pixels_fill(strip.BLACK)
    strip.pixels_show()
    time.sleep(0.05)


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
    strip.pixels_fill(strip.BLACK)
    strip.pixels_show()
    time.sleep(0.05)

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

    strip.pixels_fill(strip.BLACK)
    strip.pixels_show()
    time.sleep(0.05)    
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
       
    for color in range(0,160):
        strip.color_chase(strip.lattice[color], color)
    strip.pixels_show()
    time.sleep(0.5)
    print("rainbow")
     while(1):
    strip.rainbow_cycle(0.002)    




