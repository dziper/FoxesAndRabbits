import pygame as pg
import random
import rabbit, fox
class Grid:
    size = (None, None)
    grid = []

    def __init__(self, size):
        self.size = size
        self.grid = self.getEmpty()

    def step(self):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                animal = self.getPos((x,y))
                if animal != None:
                    animal.move()
        #move all the animals on the grid

    def getAdjacentRabbit(self,pos):
        pass
        #find an adjacent rabbit
        #if multiple, return random one

    def initializeAnimals(self, fx=5, rb=10):
        for z in range(rb):
            x = random.randint(0,self.size[0]-1)
            y = random.randint(0,self.size[1]-1)
            pos=(x,y)
            r = rabbit.Rabbit(pos, self)
        for a in range(fx):
            b = random.randint(0,self.size[0]-1)
            c = random.randint(0,self.size[1]-1)
            pos=(b,c)

            f = fox.Fox(pos, self)

        #HW:create 10 random rabbits and 5 foxes randomly
        #Add foxes and rabbits to grid randomly

    def getAdjacentEmpty(self,pos):
        empty=[]
        for x in range(pos[0]-1, pos[0]+2):
            for y in range(pos[1]-1, pos[1]+2):
                if pos==(x,y):
                    continue
                if self.isInvalidPos((x,y)):
                    continue
                if self.getPos((x,y))== None:
                    empty.append((x,y))
        length=len(empty)
        if length >= 1:
            return empty[random.randint(0,length-1)]
        else:
            return None

        #find an adjacent empty location
        #if multiple, return random one

    def getEmpty(self):
        emptyGrid = [None]*self.size[1]
        for i in range(len(emptyGrid)):
            row = [None]*self.size[0]
            emptyGrid[i] = row
        return emptyGrid

    def print(self):
        for row in self.grid:
            rowStr = ''
            for pos in row:
                if pos == None:
                    rowStr+='-'
                else:
                    rowStr+=pos.getName()
            print(rowStr)

    def add(self,animal):
        pos = animal.getPos()
        self.grid[pos[1]][pos[0]] = animal

    def remove(self,animal):
        pos = animal.getPos()
        self.grid[pos[1]][pos[0]] = None

    def isInvalidPos(self,pos):
        if pos[0]<0 or pos[0]>self.size[0]-1:
            return True
        if pos[1]<0 or pos[1]>self.size[1]-1:
            return True
        return False

    def getSurf(self,res):
        pxsize = (self.size[0]*res, self.size[1]*res)
        surf = pg.Surface(pxsize)

        for row in self.grid:
            for animal in row:
                if animal == None:
                    continue
                asurf = pg.Surface((res,res))
                asurf.fill(animal.getColor())
                pxloc = animal.getPos()
                pxloc = (pxloc[0]*res,pxloc[1]*res)
                surf.blit(asurf,pxloc)

        return surf

    def getPos(self, pos):
        return self.grid[pos[1]][pos[0]]
