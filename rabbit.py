class Rabbit:
    MAX_AGE = 4
    NAME = "R"
    BREEDING_AGE = 3
    COLOR = (200,200,0)

    def __init__(self,pos,grid):
        self.pos = pos
        self.grid = grid
        self.grid.add(self)
        self.age = 0

    def move(self):
        if self.age >= self.MAX_AGE:
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

    def getPos(self):
        return self.pos

    def die(self):
        self.grid.remove(self)

    def getName(self):
        return self.NAME

    def giveBirth(self):
        newPos = self.grid.getAdjacentEmpty(self.pos)
        if newPos == None:
            return
        baby = Rabbit(newPos,self.grid)
        baby.grid.add(baby)
        

    def getColor(self):
        return self.COLOR
