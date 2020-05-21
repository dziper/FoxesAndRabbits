import pygame as pg
import random
class Grid:
    size = (None, None)
    grid = []

    def __init__(self, size):
        self.size = size
        self.grid = self.getEmpty()

    def getEmpty(self):
        emptyGrid = [None]*self.size[1]
        for i in range(len(emptyGrid)):
            row = [None]*self.size[0]
            emptyGrid[i] = row
        return emptyGrid

    def initializeAnimals(self):
        pass

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

    def getAdjacentEmpty(self,pos):
        emptyLocs = []
        for i in range(pos[1]-1,pos[1]+2):
            for j in range(pos[0]-1,pos[0]+2):
                if self.isInvalidPos((j,i)) or pos == (i,j):
                    continue
                if self.grid[i][j] == None:
                    emptyLocs.append((j,i))
        if len(emptyLocs) == 0:
            return None
        index = random.randint(0,len(emptyLocs)-1)
        return emptyLocs[index]

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

    def step(self):
        animals = []
        for row in self.grid:
            for animal in row:
                if animal == None:
                    continue
                animals.append(animal)
        for an in animals:
            an.think()
        for an in animals:
            an.move()
