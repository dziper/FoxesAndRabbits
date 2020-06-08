import predator
Ecount=0
class Eagle(predator.Predator):
    MAX_AGE = 10
    NAME = "E"
    BREEDING_AGE = 4
    BREEDING_PROB = .5
    MAX_HUNGER = 4
    COLOR = (10,220,20)
    FOODVALUE= 2

    def __init__(self,pos,grid):
        super().__init__(pos,grid,['R'])
        global Ecount
        Ecount += 1

    def die(self):
        super().die()
        global Ecount
        Ecount -= 1
