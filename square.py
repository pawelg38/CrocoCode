import pygame

class Square(object):
    def __init__(self,surface,pixSize,color,border=0):
        self.surface = surface
        self.pixSize = pixSize
        self.color = color
        self.border = border
    def drawMe(self,pixPos):
        pygame.draw.rect(self.surface, self.color, (pixPos[0], pixPos[1], self.pixSize[0], self.pixSize[1]),self.border)