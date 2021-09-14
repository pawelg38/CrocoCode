import pygame
from random import randint
from player import Player
from treasure import Treasure
from mapElement import mapElement

mapElements = []
mapElements.append([])
mapElements[0].append(pygame.image.load("images\maps\meadow\\bonfire1.png"))
mapElements[0].append(pygame.image.load("images\maps\meadow\\bush1.png"))
mapElements[0].append(pygame.image.load("images\maps\meadow\\bush2.png"))
mapElements[0].append(pygame.image.load("images\maps\meadow\\bush3.png"))
mapElements[0].append(pygame.image.load("images\maps\meadow\\fence1.png"))
mapElements[0].append(pygame.image.load("images\maps\meadow\\flowers1.png"))
mapElements[0].append(pygame.image.load("images\maps\meadow\log1.png"))
mapElements[0].append(pygame.image.load("images\maps\meadow\stone1.png"))
mapElements[0].append(pygame.image.load("images\maps\meadow\stone2.png"))
mapElements[0].append(pygame.image.load("images\maps\meadow\stone3.png"))
mapElements[0].append(pygame.image.load("images\maps\meadow\stump1.png"))
mapElements.append([])
mapElements[1].append(pygame.image.load("images\maps\desert\\bonfire1.png"))
mapElements[1].append(pygame.image.load("images\maps\desert\cactus1.png"))
mapElements[1].append(pygame.image.load("images\maps\desert\cactus2.png"))
mapElements[1].append(pygame.image.load("images\maps\desert\cactus3.png"))
mapElements[1].append(pygame.image.load("images\maps\desert\cactus4.png"))
mapElements[1].append(pygame.image.load("images\maps\desert\cactus5.png"))
mapElements[1].append(pygame.image.load("images\maps\desert\cactus6.png"))
mapElements[1].append(pygame.image.load("images\maps\desert\cactus7.png"))
mapElements[1].append(pygame.image.load("images\maps\desert\camel1.png"))
mapElements[1].append(pygame.image.load("images\maps\desert\camel2.png"))
mapElements[1].append(pygame.image.load("images\maps\desert\camel3.png"))
mapElements[1].append(pygame.image.load("images\maps\desert\desertflower1.png"))
mapElements[1].append(pygame.image.load("images\maps\desert\desertflower2.png"))
mapElements[1].append(pygame.image.load("images\maps\desert\desertflower3.png"))
mapElements[1].append(pygame.image.load("images\maps\desert\desertflower4.png"))
mapElements.append([])
mapElements[2].append(pygame.image.load("images\maps\\beach\\bonfire1.png"))
mapElements[2].append(pygame.image.load("images\maps\\beach\\beachball1.png"))
mapElements[2].append(pygame.image.load("images\maps\\beach\\beachball2.png"))
mapElements[2].append(pygame.image.load("images\maps\\beach\\beachflower1.png"))
mapElements[2].append(pygame.image.load("images\maps\\beach\\beachpail1.png"))
mapElements[2].append(pygame.image.load("images\maps\\beach\\beachpail2.png"))
mapElements[2].append(pygame.image.load("images\maps\\beach\\bush1.png"))
mapElements[2].append(pygame.image.load("images\maps\\beach\coconut1.png"))
mapElements[2].append(pygame.image.load("images\maps\\beach\\flipflops1.png"))
mapElements[2].append(pygame.image.load("images\maps\\beach\lifebuoy1.png"))
mapElements[2].append(pygame.image.load("images\maps\\beach\palm1.png"))
mapElements[2].append(pygame.image.load("images\maps\\beach\palm2.png"))
mapElements[2].append(pygame.image.load("images\maps\\beach\palm3.png"))
mapElements[2].append(pygame.image.load("images\maps\\beach\palm4.png"))
mapElements[2].append(pygame.image.load("images\maps\\beach\palm5.png"))
mapElements[2].append(pygame.image.load("images\maps\\beach\shell1.png"))
mapElements[2].append(pygame.image.load("images\maps\\beach\shell2.png"))
mapElements[2].append(pygame.image.load("images\maps\\beach\\umbrella1.png"))
mapElements[2].append(pygame.image.load("images\maps\\beach\\umbrella2.png"))
mapElements[2].append(pygame.image.load("images\maps\\beach\\umbrella3.png"))

class Map(object):
    def __init__(self,surface,pixPos,pixSize,grid,color,difficulty):
        self.surface = surface
        self.pixPos = pixPos
        self.pixSize = pixSize
        self.grid = grid
        self.color = color
        self.difficulty = difficulty
        self.mapImages = []
        self.mapImages.append(pygame.image.load("images\maps\meadow\meadowEasy.png").convert())
        self.mapImages.append(pygame.image.load("images\maps\desert\desertEasy.png").convert())
        self.mapImages.append(pygame.image.load("images\maps\\beach\\beachEasy.png").convert())
        self.mapImages.append(pygame.image.load("images\maps\meadow\meadowMedium.png").convert())
        self.mapImages.append(pygame.image.load("images\maps\desert\desertMedium.png").convert())
        self.mapImages.append(pygame.image.load("images\maps\\beach\\beachMedium.png").convert())
        self.mapImages.append(pygame.image.load("images\maps\meadow\meadowHard.png").convert())
        self.mapImages.append(pygame.image.load("images\maps\desert\desertHard.png").convert())
        self.mapImages.append(pygame.image.load("images\maps\\beach\\beachHard.png").convert())
        if self.difficulty == 0:
            self.rnMap = randint(0,2)
            self.rnMapModel = self.rnMap
            self.mapImage = self.mapImages[self.rnMap]
        elif self.difficulty == 1:
            self.rnMap = randint(3,5)
            self.rnMapModel = self.rnMap-3
            self.mapImage = self.mapImages[self.rnMap]
        elif self.difficulty == 2:
            self.rnMap = randint(6,8)
            self.rnMapModel = self.rnMap-6
            self.mapImage = self.mapImages[self.rnMap]

        self.path = []

        self.gridElements = []
        self.gridElements_pixPos = []
        for row in range(self.grid[0]):
            self.gridElements.append([])
            self.gridElements_pixPos.append([])
            for column in range(self.grid[1]):
                self.gridElements_pixPos[row].append((self.pixPos[0]+row*51,self.pixPos[1]+column*51))
                self.gridElements[row].append([])
        for row in range(self.grid[0]):
            for column in range(self.grid[1]):
                los = randint(0,9)
                if los > 6:
                    e = randint(0, len(mapElements[self.rnMapModel])-1)
                    self.gridElements[row][column] = mapElement(self,(row,column),(50,50),mapElements[self.rnMapModel][e])
        #print(self.gridElements_pixPos)
        ## Player ##
        if self.difficulty == 0:
            self.px = randint(0,3)
            self.py = randint(0,3)
            self.tx = randint(5,7)
            self.ty = randint(0,5)
        elif self.difficulty == 1:
            self.px = randint(0,3)
            self.py = randint(0,8)
            self.tx = randint(9,11)
            self.ty = randint(0,8)
        elif self.difficulty == 2:
            self.px = randint(0,3)
            self.py = randint(0,11)
            self.tx = randint(13,15)
            self.ty = randint(0,11)
        self.player = Player(self, (self.px,self.py), (50, 50), (255, 255, 255))
        self.treasure = Treasure(self, (self.tx,self.ty), (50, 50), (255, 255, 255), True)
        ## Player ##
        self.findWay()
    def findWay(self):
        P = []
        visited = []
        S = []
        vS = self.player.gridPos
        vK = self.treasure.gridPos
        if self.difficulty == 0:
            gridWidth = 8
            gridHeight = 6
        elif self.difficulty == 1:
            gridWidth = 12
            gridHeight = 9
        elif self.difficulty == 2:
            gridWidth = 16
            gridHeight = 12
        for i in range(gridWidth):
            P.append([])
            visited.append([])
            for j in range(gridHeight):
                P[i].append(False)
                visited[i].append(False)
        P[vS[0]][vS[1]] = (-1, -1)
        S.append(vS)
        visited[vS[0]][vS[1]] = True
        while (len(S)):
            v = S.pop()
            if v == vK:
                break
            vNeighbours = [(v[0] - 1, v[1]), (v[0], v[1] - 1), (v[0] + 1, v[1]), (v[0], v[1] + 1)]
            while (len(vNeighbours)):
                rN = randint(0, len(vNeighbours) - 1)
                neighbour = vNeighbours[rN]
                if neighbour[0] >= 0 and neighbour[0] <= gridWidth-1 and neighbour[1] >= 0 and neighbour[1] <= gridHeight-1:
                    if visited[neighbour[0]][neighbour[1]] != True:
                        P[neighbour[0]][neighbour[1]] = v
                        S.append(neighbour)
                        visited[neighbour[0]][neighbour[1]] = True
                vNeighbours.pop(rN)
        while v != (-1, -1):
            self.path.append(v)
            v = P[v[0]][v[1]]
        for step in self.path[1:-1]:
            if self.gridElements[step[0]][step[1]] != []:
                self.gridElements[step[0]][step[1]] = []
    def drawMe(self):
        pygame.draw.rect(self.surface,self.color,(self.pixPos[0],self.pixPos[1],self.pixSize[0],self.pixSize[1]))
        self.surface.blit(self.mapImage,self.pixPos)
        for row in range(self.grid[0]):
            for column in range(self.grid[1]):
                if self.gridElements[row][column] != [] and self.gridElements[row][column] != False:
                    self.gridElements[row][column].drawMe(self.gridElements_pixPos[row][column])