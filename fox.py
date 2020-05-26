import random
class Fox:
    MAX_AGE = 10
    NAME = "F"
    BREEDING_AGE = 5
    BREEDING_PROB = .4
    MAX_HUNGER = 3
    COLOR = (0,0,200)

    def __init__(self,pos,grid):
        self.pos = pos
        self.grid = grid
        self.grid.add(self)
        self.age = 0
        self.hunger = self.MAX_HUNGER

    def move(self):
        self.grid.remove(self)
        position = self.grid.getAdjacentEmpty(self.pos)
        if position == None:
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
        self.hunt()

        #Hunt or Move the Fox to an adjacent empty location
        #increment age, hunger, die if too old, hungry, or crowded
        #give birth if of age

    def hunt(self):
        self.grid.getAdjacentRabbit()
        #find a rabbit and kill it >;)

    def giveBirth(self):
        if random.random() < self.BREEDING_PROB:
            position=self.grid.getAdjacentEmpty(self.pos)
            if position == None:
                self.die()
                return
            f = Fox(position, self.grid)
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
