import random

HEADS = 1
TAIlS = 2
TOSSES = 10

def tosses_coin():
    for toss in range(TOSSES):
        if random.randint(HEADS, TAIlS) == HEADS:
            print('Heads')
        else :
            print('TAIlS')
            
tosses_coin() 