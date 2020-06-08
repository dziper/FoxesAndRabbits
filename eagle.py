import predator
class Eagle(predator.Predator):
    MAX_AGE = 10
    NAME = "E"
    BREEDING_AGE = 4
    BREEDING_PROB = .5
    MAX_HUNGER = 4
    COLOR = (220,220,220)
    FOODVALUE= 2

    def __init__(self,pos,grid):
        super().__init__(pos,grid,['R'])