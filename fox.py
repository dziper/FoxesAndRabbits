import predator

Fcount=0

class Fox(predator.Predator):
    MAX_AGE = 10
    NAME = "F"
    BREEDING_AGE = 5
    BREEDING_PROB = .6
    MAX_HUNGER = 5
    COLOR = (200,0,0)
    FOODVALUE= 4


    def __init__(self,pos,grid):
        super().__init__(pos,grid,['R', 'E'])
        global Fcount
        Fcount += 1

    def die(self):
        super().die()
        global Fcount
        Fcount -= 1
