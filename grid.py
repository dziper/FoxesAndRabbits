
class Grid:
    size = (None, None)
    grid = []

    def __init__(self, size):
        self.size = size
        self.grid = self.getEmpty()

    def getEmpty(self):
        emptyGrid = [None]*self.size[0]
        for i in range(len(emptyGrid)):
            row = [None]*self.size[1]
            emptyGrid[i] = row
        return emptyGrid

    def print(self):
        for row in self.grid:
            print(row)

    def add(self,animal):
        pos = animal.getLoc()
        self.grid[pos[0]][pos[1]] = animal
        
