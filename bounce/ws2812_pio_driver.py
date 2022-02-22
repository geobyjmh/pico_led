#https://github.com/geobyjmh/pico_led

#I found the code in this file a little confusing to start with, that was until I realised the code was not running on the
#Raspberry Pi Pico itself but a dedicated hardware peripheral for controlling the I/O.
#The links below will help you understand this I/O peripheral:
#https://www.seeedstudio.com/blog/2021/01/25/programmable-io-with-raspberry-pi-pico/
#https://youtu.be/yYnQYF_Xa8g

from machine import Pin
import rp2

PIN_NUM = 6
NUMBER_OF_LEDS = 160


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
    
    
def create_and_run_pio_statemachine():
    global sm
    sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))
    sm.active(1)
    return sm

def write_to_neopixel(array_data):
    global sm
    sm.put(array_data, 8)
    
def get_number_of_leds():
    return NUMBER_OF_LEDS
    