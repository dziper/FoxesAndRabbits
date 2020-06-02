import animal
class Predator(animal.Animal):

    def __init__(self,pos,grid,prey):
        super().__init__(pos,grid,self.__class__)
        self.hunger = 0
        self.prey=prey

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
        prey=self.grid.getAdjacentAnimal(self.pos, self.prey)
        if prey != None:
            prey.die()
            self.hunger = 0

        #find a rabbit and kill it >;)
