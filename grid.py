
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
        if pos[0]<0 or pos[0]>self.size[0]:
            return True
        if pos[1]<0 or pos[1]>self.size[1]:
            return True
        return False

    def getAdjacentEmpty(self,pos):
        for i in range(pos[1]-1,pos[1]+2):
            for j in range(pos[0]-1,pos[0]+2):
                if self.isInvalidPos((i,j)) or pos == (i,j):
                    continue
                if self.grid[i][j] == None:
                    return (j,i)
        return None
