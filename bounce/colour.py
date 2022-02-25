#https://github.com/geobyjmh/pico_led
import random
 
BLACK = (0, 0, 0)
RED = (15, 0, 0)
YELLOW = (15, 15, 0)
GREEN = (0, 15, 0)
CYAN = (0, 15, 15)
BLUE = (0, 0, 15)
PURPLE = (15, 0, 15)
WHITE = (15, 15, 15)

COLORS = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]

def get_random_colour():
    return COLORS[random.randint(0,len(COLORS)-1)]
    
        