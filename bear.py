import predator
class Bear(predator.Predator):
    MAX_AGE = 15
    NAME = "B"
    BREEDING_AGE = 10
    BREEDING_PROB = .5
    MAX_HUNGER = 7
    COLOR = (0,200,0)

    def __init__(self,pos,grid):
        super().__init__(pos,grid,['R','F', 'W'])
