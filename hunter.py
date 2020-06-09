import predator
Hcount=0
class Hunter(predator.Predator):
    MAX_AGE = 16
    NAME = "H"
    BREEDING_AGE = 7
    BREEDING_PROB = .5
    MAX_HUNGER = 7
    COLOR = (100,100,100)
    FOODVALUE= 8

    def __init__(self,pos,grid):
        super().__init__(pos,grid,['R','E'])
        global Hcount
        Hcount += 1

    def die(self):
        super().die()
        global Hcount
        Hcount -= 1
