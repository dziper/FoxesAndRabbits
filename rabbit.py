import random
import animal
class Rabbit(animal.Animal):
    MAX_AGE = 5
    NAME = "R"
    BREEDING_AGE = 2
    BREEDING_PROB= .4
    COLOR = (255,200,0)

    def __init__(self,pos,grid):
        super().__init__(pos,grid,self.__class__)
