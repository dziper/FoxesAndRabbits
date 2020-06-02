import random
import animal
class Fox(animal.Animal):
    MAX_AGE = 10
    NAME = "F"
    BREEDING_AGE = 5
    BREEDING_PROB = .6
    MAX_HUNGER = 5
    COLOR = (200,0,0)

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

        #Hunt or Move the Fox to an adjacent empty location
        #increment age, hunger, die if too old, hungry, or crowded
        #give birth if of age

    def hunt(self):
        rb=self.grid.getAdjacentAnimal(self.pos, ['R'])
        if rb != None:
            rb.die()
            self.hunger = 0

        #find a rabbit and kill it >;)

    
