import random
class Rabbit:
    MAX_AGE = 10
    NAME = "R"
    BREEDING_AGE = 5
    BREEDING_PROB= .4
    COLOR = (200,200,0)

    def __init__(self,pos,grid):
        self.pos = pos
        self.grid = grid
        self.grid.add(self)
        self.age = 0

    def move(self):
        pass
        #Hunt or Move the Rabbit to an adjacent empty location
        #increment age, die if too old, or crowded
        #give birth if of age

    def giveBirth(self):
        pass
        #Give birth to a baby fox in adj empt loc

    def getPos(self):
        return self.pos

    def die(self):
        self.grid.remove(self)

    def getName(self):
        return self.NAME

    def getColor(self):
        return self.COLOR

    def think(self):
        pass
