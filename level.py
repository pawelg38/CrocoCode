import pygame
from map import Map
from textBox import TextBox
from button import Button

class Level(object):
    def __init__(self,surface,lvlNum,fonts,game,difficulty):
        self.game = game
        self.difficulty = difficulty
        self.surface = surface
        self.lvlNum = lvlNum
        self.fonts = fonts

        self.helpToogle = False
        # Creating objects #
        ## Map ##
        if self.difficulty == 0:
            self.map = Map(self.surface,(204,193),(408,306),(8,6),(0,255,0),self.difficulty)
        elif self.difficulty == 1:
            self.map = Map(self.surface,(102,116),(612,459),(12,9),(0,255,0),self.difficulty)
        elif self.difficulty == 2:
            self.map = Map(self.surface,(0,40),(816,612),(16,12),(0,255,0),self.difficulty)
        ## Map ##
        ## TextBox ##
        self.textBox = TextBox(self,self.surface,(400,612),(255,255,255),(0,90,130),(0,40,80),self.fonts[0],self.game)
        ## TextBox ##
        ## Buttons ##
        self.buttonRunImg = pygame.image.load("images/buttons/buttonRun.png")
        self.buttonRunImgHl = pygame.image.load("images/buttons/buttonRun_hl.png")
        self.buttonRun = Button(self.surface,(850,652),(140,59),img=self.buttonRunImg,img_hl=self.buttonRunImgHl)
        self.buttonHelp2Img = pygame.image.load("images/buttons/buttonHelp2.png")
        self.buttonHelp2ImgHl = pygame.image.load("images/buttons/buttonHelp2_hl.png")
        self.buttonHelp2 = Button(self.surface,(1050,652),(140,59),img=self.buttonHelp2Img,img_hl=self.buttonHelp2ImgHl)
        self.buttonMenuImg = pygame.image.load("images/buttons/buttonMenu.png")
        self.buttonMenuImgHl = pygame.image.load("images/buttons/buttonMenu_hl.png")
        self.buttonMenu = Button(self.surface,(10,652),(140,59),img=self.buttonMenuImg,img_hl=self.buttonMenuImgHl)
        ## Buttons ##
        ## Level ##
        self.textLvlNum = self.fonts[3].render("Level "+str(self.lvlNum+1),1,(120,40,0))
        ## Level ##
        # Creating objects #

    def drawMe(self):
        self.surface.blit(pygame.image.load("images/misc/wood2_70x800.png"),(800,0))
        self.surface.blit(pygame.image.load("images/misc/wood2_70x800.png"),(1230,0))
        self.map.drawMe()
        self.textBox.drawMe((850,40))
        self.surface.blit(pygame.image.load("images/misc/wood2_1400x70.png"),(-24,-26))
        self.surface.blit(pygame.image.load("images/misc/wood2_1400x100.png"),(-24,640))
        self.buttonRun.drawMe()
        self.buttonHelp2.drawMe()
        self.buttonMenu.drawMe()
        self.textLvlNum = self.fonts[3].render("Level " + str(self.lvlNum + 1), 1, (120, 40, 0))
        self.surface.blit(self.textLvlNum,(560,0))
    def buttonRun_clickAction1(self):
        self.buttonRun.buttonRun_clickAction1(self.textBox,self.map,self.map.player,self.game)
    def buttonMenu_clickAction1(self):
        self.buttonMenu.buttonMenu_clickAction1(self.game)
        self.game.helpToogle = False
    def buttonHelp2_clickAction1(self):
        self.buttonHelp2.buttonHelp2_clickAction1(self.game)
    def wylaczPomoc2(self):
        if self.helpToogle == True:
            self.helpToogle = False
        elif self.helpToogle == False:
            self.helpToogle = True