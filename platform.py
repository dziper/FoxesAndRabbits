
class Platform():
    COLOR = (200,0,0)


    def __init__(self, pos):
        self.size= int(w*h/res)
        self.pos = pos

    def Left(self):
        self.pos = (self.pos[0]-5, self.pos[1])
    def Right(self):
        self.pos = (self.pos[0]+5, self.pos[1])

    def getPos(self):
        return self.pos
