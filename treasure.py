import pygame
from square import Square

class Treasure(object):
    def __init__(self,map,gridPos,pixSize,color,closed):
        self.surface = map.surface
        self.map = map
        self.pixSize = pixSize
        self.gridPos = gridPos
        self.color = color
        self.closed = closed
        self.playerGot = False

        self.body = Square(self.surface,self.pixSize,self.color)
        self.map.gridElements[self.gridPos[0]][self.gridPos[1]] = self

        if closed:
            self.bodyImage = pygame.image.load("images/treasure/treasure1.png")
        else:
            self.bodyImage = pygame.image.load("images/treasure/treasure2.png")

    def drawMe(self, pixPos):
        if self.playerGot == False:
            if self.closed:
                self.bodyImage = pygame.image.load("images/treasure/treasure1.png")
            else:
                self.bodyImage = pygame.image.load("images/treasure/treasure2.png")
            self.surface.blit(self.bodyImage,pixPos)