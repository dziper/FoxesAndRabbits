import random
class Animal:

    def __init__(self,pos,grid,type):
        self.pos = pos
        self.grid = grid
        self.grid.add(self)
        self.age = 0
        self.dying = False
        self.type = type

    def move(self):
        self.grid.remove(self)
        position = self.grid.getAdjacentEmpty(self.pos)
        if position == None or self.dying:
            self.die()
            return
        self.pos = position
        self.grid.add(self)
        self.age=self.age+1
        if self.age == self.MAX_AGE:
            self.die()
            return
        if self.age >= self.BREEDING_AGE:
            self.giveBirth()
        #increment age, die if too old, or crowded
        #give birth if of age

    def giveBirth(self):

        if random.random() < self.BREEDING_PROB:
            position=self.grid.getAdjacentEmpty(self.pos)
            if position == None:
                self.die()
                return
            r = self.type(position, self.grid)

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
        position = self.grid.getAdjacentEmpty(self.pos)
        if position == None:
            self.dying = True
