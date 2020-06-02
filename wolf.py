import predator
class Wolf(predator.Predator):
    MAX_AGE = 10
    NAME = "W"
    BREEDING_AGE = 5
    BREEDING_PROB = .4
    MAX_HUNGER = 5
    COLOR = (0,0,200)
    FOODVALUE= 5

    def __init__(self,pos,grid):
        super().__init__(pos,grid,['F'])
