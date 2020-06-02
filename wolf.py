import random
import animal
class Wolf(animal.Animal):
    MAX_AGE = 14
    NAME = "W"
    BREEDING_AGE = 5
    BREEDING_PROB = .4
    MAX_HUNGER = 6
    COLOR = (0,0,200)

    def __init__(self,pos,grid):
        super().__init__(pos,grid,self.__class__)
        self.hunger = 0

    def move(self):
        super().move()
        self.hunger=self.hunger+1
        self.hunt()
        if self.hunger >= self.MAX_HUNGER:
            self.die()
            return
    def hunt(self):
        fx=self.grid.getAdjacentAnimal(self.pos, ['F'])
        if fx != None:
            fx.die()
            self.hunger = 0
