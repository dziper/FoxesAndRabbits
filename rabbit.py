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


    def giveBirth(self):

        if random.random() < self.BREEDING_PROB:
            position=self.grid.getAdjacentEmpty(self.pos)
            r = Rabbit(position, self.grid)

            #Give birth to a baby rabbit in adj empt loc

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

    def move(self):
        self.grid.remove(self)
        self.pos = self.grid.getAdjacentEmpty(self.pos)
        self.grid.add(self)
        self.age=self.age+1
        if self.age == self.MAX_AGE:
            self.die()
        if self.age >= self.BREEDING_AGE:
            self.giveBirth()
        #increment age, die if too old, or crowded
        #give birth if of age
