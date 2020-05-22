import random
class Fox:
    MAX_AGE = 10
    NAME = "F"
    BREEDING_AGE = 5
    BREEDING_PROB= .4
    COLOR = (0,0,200)

    def __init__(self,pos,grid):
        self.pos = pos
        self.grid = grid
        self.grid.add(self)
        self.age = 0

    def move(self):
        if self.age >= self.MAX_AGE or self.dying:
            self.die()
            return
        if self.age >= self.BREEDING_AGE:
            self.giveBirth()
        self.age += 1
        newPos = self.grid.getAdjacentEmpty(self.pos)
        if newPos == None:
            self.die()
        else:
            self.grid.remove(self)
            self.pos = newPos
            self.grid.add(self)

    def think(self):
        newPos = self.grid.getAdjacentEmpty(self.pos)
        if newPos == None:
            self.dying = True
        else:
            self.dying = False

    def getPos(self):
        return self.pos

    def die(self):
        self.grid.remove(self)

    def getName(self):
        return self.NAME

    def giveBirth(self):
        if random.random()<self.BREEDING_PROB:
            newPos = self.grid.getAdjacentEmpty(self.pos)
            if newPos == None:
                return
            baby = Fox(newPos,self.grid)

    def getColor(self):
        return self.COLOR
