import random
import animal

Rcount = 0

class Rabbit(animal.Animal):
    MAX_AGE = 6
    NAME = "R"
    BREEDING_AGE = 2
    BREEDING_PROB= .6
    COLOR = (255,200,0)
    FOODVALUE= 1

    def __init__(self,pos,grid):
        super().__init__(pos,grid,self.__class__)
        global Rcount
        Rcount += 1

    def die(self):
        super().die()
        global Rcount
        Rcount -= 1
