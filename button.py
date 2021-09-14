import sys
import pygame

class Button(object):
    def __init__(self,surface,pixPos,pixSize,fgColor=False,bSize=False,bColor=False,text=False,textColor=False,font=False,img=False,img_hl=False):
        self.surface = surface
        self.pixPos = pixPos
        self.pixSize = pixSize
        self.fgColor = fgColor
        self.tmpFgColor = fgColor
        self.bSize = bSize
        self.bColor = bColor
        self.tmpBColor = bColor
        self.textColor = textColor
        self.font = font
        if text:
            self.text = self.font.render(text, 1, textColor)
        self.arialFont = pygame.font.SysFont('arial', 20)
        self.img = img
        self.img_hl = img_hl

    def drawMe(self):
        if self.img and self.img_hl:
            mousePos = pygame.mouse.get_pos()
            if(mousePos[0] >= self.pixPos[0] and mousePos[0] <= self.pixPos[0]+self.pixSize[0] and mousePos[1] >= self.pixPos[1] and mousePos[1] <= self.pixPos[1]+self.pixSize[1]):
                self.surface.blit(self.img_hl,self.pixPos)
            else:
                self.surface.blit(self.img,self.pixPos)
        elif self.img and not self.img_hl:
            mousePos = pygame.mouse.get_pos()
            if(mousePos[0] >= self.pixPos[0] and mousePos[0] <= self.pixPos[0]+self.pixSize[0] and mousePos[1] >= self.pixPos[1] and mousePos[1] <= self.pixPos[1]+self.pixSize[1]):
                self.surface.blit(self.img,self.pixPos)
            else:
                self.surface.blit(self.img, self.pixPos)
        else:
            pygame.draw.rect(self.surface,self.fgColor,(self.pixPos[0],self.pixPos[1],self.pixSize[0],self.pixSize[1]))
            if self.bSize:
                pygame.draw.rect(self.surface,self.bColor,(self.pixPos[0],self.pixPos[1],self.pixSize[0],self.pixSize[1]),1)
            self.surface.blit(self.text, (self.pixPos[0]+(self.pixSize[0]/2)-(self.text.get_width()/2),self.pixPos[1]+(self.pixSize[1]/2)-(self.text.get_height()/2)))
            mousePos = pygame.mouse.get_pos()
            if(mousePos[0] >= self.pixPos[0] and mousePos[0] <= self.pixPos[0]+self.pixSize[0] and mousePos[1] >= self.pixPos[1] and mousePos[1] <= self.pixPos[1]+self.pixSize[1]):
                self.fgColor = (150,255,255)
                self.bColor = (0,0,0)
            else:
                self.fgColor = self.tmpFgColor
                self.bColor = self.tmpBColor
    def buttonRun_clickAction1(self,textBox,map,player,game):
        mousePos = pygame.mouse.get_pos()
        if(mousePos[0] >= self.pixPos[0] and mousePos[0] <= self.pixPos[0]+self.pixSize[0] and mousePos[1] >= self.pixPos[1] and mousePos[1] <= self.pixPos[1]+self.pixSize[1]):
            if game.menu == False:
                textBox.analizeCode(map,player)
    def buttonMenu_clickAction1(self,game):
        mousePos = pygame.mouse.get_pos()
        if(mousePos[0] >= self.pixPos[0] and mousePos[0] <= self.pixPos[0] + self.pixSize[0] and mousePos[1] >= self.pixPos[1] and mousePos[1] <= self.pixPos[1] + self.pixSize[1]):
            if game.menu == False:
                game.menu = True
    def buttonStart_clickAction1(self,game):
        mousePos = pygame.mouse.get_pos()
        if(mousePos[0] >= self.pixPos[0] and mousePos[0] <= self.pixPos[0]+self.pixSize[0] and mousePos[1] >= self.pixPos[1] and mousePos[1] <= self.pixPos[1]+self.pixSize[1]):
            if game.menu == True:
                game.chooseDifficulty()
    def buttonEasyLevel_clickAction1(self,game):
        mousePos = pygame.mouse.get_pos()
        if(mousePos[0] >= self.pixPos[0] and mousePos[0] <= self.pixPos[0]+self.pixSize[0] and mousePos[1] >= self.pixPos[1] and mousePos[1] <= self.pixPos[1]+self.pixSize[1]):
            if game.menu == True:
                game.difficultyLvl = 0
                game.newLevel()
                game.difficultySelection = False
                game.menu = False
    def buttonMediumLevel_clickAction1(self,game):
        mousePos = pygame.mouse.get_pos()
        if(mousePos[0] >= self.pixPos[0] and mousePos[0] <= self.pixPos[0]+self.pixSize[0] and mousePos[1] >= self.pixPos[1] and mousePos[1] <= self.pixPos[1]+self.pixSize[1]):
            if game.menu == True:
                game.difficultyLvl = 1
                game.newLevel()
                game.difficultySelection = False
                game.menu = False
    def buttonHardLevel_clickAction1(self,game):
        mousePos = pygame.mouse.get_pos()
        if(mousePos[0] >= self.pixPos[0] and mousePos[0] <= self.pixPos[0]+self.pixSize[0] and mousePos[1] >= self.pixPos[1] and mousePos[1] <= self.pixPos[1]+self.pixSize[1]):
            if game.menu == True:
                game.difficultyLvl = 2
                game.newLevel()
                game.difficultySelection = False
                game.menu = False
    def buttonQuit_clickAction1(self,game):
        mousePos = pygame.mouse.get_pos()
        if(mousePos[0] >= self.pixPos[0] and mousePos[0] <= self.pixPos[0]+self.pixSize[0] and mousePos[1] >= self.pixPos[1] and mousePos[1] <= self.pixPos[1]+self.pixSize[1]):
            if game.menu == True:
                pygame.quit()
                sys.exit()
    def buttonHelp_clickAction1(self,game):
        mousePos = pygame.mouse.get_pos()
        if(mousePos[0] >= self.pixPos[0] and mousePos[0] <= self.pixPos[0]+self.pixSize[0] and mousePos[1] >= self.pixPos[1] and mousePos[1] <= self.pixPos[1]+self.pixSize[1]):
            game.wylaczPomoc()
    def buttonHelp2_clickAction1(self,game):
        mousePos = pygame.mouse.get_pos()
        if(mousePos[0] >= self.pixPos[0] and mousePos[0] <= self.pixPos[0]+self.pixSize[0] and mousePos[1] >= self.pixPos[1] and mousePos[1] <= self.pixPos[1]+self.pixSize[1]):
            game.level.wylaczPomoc2()
    def buttonMusicOn_clickAction1(self,game):
        mousePos = pygame.mouse.get_pos()
        if(mousePos[0] >= self.pixPos[0] and mousePos[0] <= self.pixPos[0]+self.pixSize[0] and mousePos[1] >= self.pixPos[1] and mousePos[1] <= self.pixPos[1]+self.pixSize[1]):
            if game.musicToogle == False:
                game.musicToogle = True
                pygame.mixer.music.play(-1)
    def buttonMusicOff_clickAction1(self,game):
        mousePos = pygame.mouse.get_pos()
        if(mousePos[0] >= self.pixPos[0] and mousePos[0] <= self.pixPos[0]+self.pixSize[0] and mousePos[1] >= self.pixPos[1] and mousePos[1] <= self.pixPos[1]+self.pixSize[1]):
            if game.musicToogle == True:
                game.musicToogle = False
                pygame.mixer.music.stop()