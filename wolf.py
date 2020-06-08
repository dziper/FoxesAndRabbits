import predator
Wcount=0
class Wolf(predator.Predator):
    MAX_AGE = 10
    NAME = "W"
    BREEDING_AGE = 5
    BREEDING_PROB = .7
    MAX_HUNGER = 5
    COLOR = (0,0,200)
    FOODVALUE= 5

    def __init__(self,pos,grid):
        super().__init__(pos,grid,['F'])
        global Wcount
        Wcount += 1

    def die(self):
        super().die()
        global Wcount
        Wcount -= 1
