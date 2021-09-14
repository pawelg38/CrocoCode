import pygame
from square import Square

class Player(object):
    def __init__(self,map,gridPos,pixSize,color):
        self.surface = map.surface
        self.map = map
        self.pixSize = pixSize
        self.map = map
        self.gridPos = gridPos
        self.color = color
        self.turn = "left"
        self.gotTreasure = False
        self.defaultGridPos = gridPos

        self.body = Square(self.surface,self.pixSize,self.color)
        self.map.gridElements[self.gridPos[0]][self.gridPos[1]] = self

        self.playerImage = pygame.image.load("images/croco/croco1left.png")

    def drawMe(self, pixPos):
        self.surface.blit(self.playerImage,pixPos)
    def turnLeft(self):
        self.turn = "left"
        self.playerImage = pygame.image.load("images/croco/croco1left.png")
    def turnRight(self):
        self.turn = "right"
        self.playerImage = pygame.image.load("images/croco/croco1right.png")
    def resetPosition(self):
        self.map.gridElements[self.gridPos[0]][self.gridPos[1]] = []
        self.gridPos = self.defaultGridPos
        self.map.gridElements[self.gridPos[0]][self.gridPos[1]] = self
    def goLeft(self):
        if self.gridPos[0] != 0:
            if self.turn == "left":
                newGridPos = (self.gridPos[0]-1, self.gridPos[1])
                if self.map.gridElements[newGridPos[0]][newGridPos[1]] == []:
                    self.map.gridElements[self.gridPos[0]][self.gridPos[1]] = []
                    self.gridPos = newGridPos
                    self.map.gridElements[newGridPos[0]][newGridPos[1]] = self
    def goRight(self):
        if self.gridPos[0] != 15:
            if self.turn == "right":
                newGridPos = (self.gridPos[0]+1, self.gridPos[1])
                if self.map.gridElements[newGridPos[0]][newGridPos[1]] == []:
                    self.map.gridElements[self.gridPos[0]][self.gridPos[1]] = []
                    self.gridPos = newGridPos
                    self.map.gridElements[newGridPos[0]][newGridPos[1]] = self
    def goUp(self):
        if self.gridPos[1] != 0:
            newGridPos = (self.gridPos[0], self.gridPos[1]-1)
            if self.map.gridElements[newGridPos[0]][newGridPos[1]] == []:
                self.map.gridElements[self.gridPos[0]][self.gridPos[1]] = []
                self.gridPos = newGridPos
                self.map.gridElements[newGridPos[0]][newGridPos[1]] = self
    def goDown(self):
        if self.gridPos[1] != 11:
            newGridPos = (self.gridPos[0], self.gridPos[1]+1)
            if self.map.gridElements[newGridPos[0]][newGridPos[1]] == []:
                self.map.gridElements[self.gridPos[0]][self.gridPos[1]] = []
                self.gridPos = newGridPos
                self.map.gridElements[newGridPos[0]][newGridPos[1]] = self
    def control(self,eventKey):
        if eventKey == pygame.K_LEFT:
            if self.gridPos[0] != 0:
                newGridPos = (self.gridPos[0]-1, self.gridPos[1])
                self.map.gridElements[self.gridPos[0]][self.gridPos[1]] = []
                self.gridPos = newGridPos
                self.map.gridElements[newGridPos[0]][newGridPos[1]] = self
        elif eventKey == pygame.K_RIGHT:
            if self.gridPos[0] != 15:
                newGridPos = (self.gridPos[0]+1, self.gridPos[1])
                self.map.gridElements[self.gridPos[0]][self.gridPos[1]] = []
                self.gridPos = newGridPos
                self.map.gridElements[newGridPos[0]][newGridPos[1]] = self
        elif eventKey == pygame.K_UP:
            if self.gridPos[1] != 0:
                newGridPos = (self.gridPos[0], self.gridPos[1]-1)
                self.map.gridElements[self.gridPos[0]][self.gridPos[1]] = []
                self.gridPos = newGridPos
                self.map.gridElements[newGridPos[0]][newGridPos[1]] = self
        elif eventKey == pygame.K_DOWN:
            if self.gridPos[1] != 11:
                newGridPos = (self.gridPos[0], self.gridPos[1]+1)
                self.map.gridElements[self.gridPos[0]][self.gridPos[1]] = []
                self.gridPos = newGridPos
                self.map.gridElements[newGridPos[0]][newGridPos[1]] = self