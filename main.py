import sys
import pygame
from level import Level
from button import Button

class Game(object):
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Praca inzynierska - CrocoCode")
        self.res = (1280,720)
        self.mainSurface = pygame.display.set_mode(self.res)
        clock = pygame.time.Clock()

        # Creating objects #
        ## Background ##
        self.menu = True
        self.menuBg = pygame.image.load("images/background/menuBackground_2.png")
        self.helpToogle = False
        ## Background ##
        ## Buttons ##
        self.buttonStartImg = pygame.image.load("images/buttons/buttonStart.png")
        self.buttonStartImgHl = pygame.image.load("images/buttons/buttonStart_hl.png")
        self.buttonQuitImg = pygame.image.load("images/buttons/buttonQuit.png")
        self.buttonQuitImgHl = pygame.image.load("images/buttons/buttonQuit_hl.png")

        self.buttonStart = Button(self.mainSurface,(440,151),(400,209),img=self.buttonStartImg,img_hl=self.buttonStartImgHl)
        self.buttonQuit = Button(self.mainSurface,(49,526),(266,139),img=self.buttonQuitImg,img_hl=self.buttonQuitImgHl)
        ## Buttons ##
        ## Help ##
        self.helpImg = pygame.image.load("images/help/help.png")
        self.buttonHelpImg = pygame.image.load("images/buttons/buttonHelp.png")
        self.buttonHelpImgHl = pygame.image.load("images/buttons/buttonHelp_hl.png")
        self.buttonHelp = Button(self.mainSurface,(349,526),(266,139),img=self.buttonHelpImg,img_hl=self.buttonHelpImgHl)
        ## Help ##
        ## Fonts ##
        self.fonts = []
        self.fonts.append(pygame.font.SysFont('centurygothic', 20))
        self.fonts.append(pygame.font.SysFont('comicsansms', 20))
        self.fonts.append(pygame.font.SysFont('arial', 20))
        self.fonts.append(pygame.font.SysFont('arial', 36))
        self.textMusic = self.fonts[1].render("Music: www.bensound.com",1,(0,0,0))
        ## Fonts ##
        ## Music ##
        pygame.mixer.music.load("music/bensound-littleidea.mp3")

        self.buttonMusicOnImg = pygame.image.load("images/buttons/speakerOn.png")
        self.buttonMusicOffImg = pygame.image.load("images/buttons/speakerOff.png")

        self.buttonMusicOn = Button(self.mainSurface,(255,5),(59,40),img=self.buttonMusicOnImg)
        self.buttonMusicOff = Button(self.mainSurface,(255,5),(38,40),img=self.buttonMusicOffImg)

        self.musicToogle = False
        ## Music ##
        ## Levels ##
        self.difficultySelectionImg = pygame.image.load("images/difficultySelection/difficultySelection.png")
        self.easyLevelImg = pygame.image.load("images/difficultySelection/easy.png")
        self.easyLevelImgHl = pygame.image.load("images/difficultySelection/easy_hl.png")
        self.mediumLevelImg = pygame.image.load("images/difficultySelection/medium.png")
        self.mediumLevelImgHl = pygame.image.load("images/difficultySelection/medium_hl.png")
        self.hardLevelImg = pygame.image.load("images/difficultySelection/hard.png")
        self.hardLevelImgHl = pygame.image.load("images/difficultySelection/hard_hl.png")

        self.buttonEasyLevel = Button(self.mainSurface,(490,200),(300,90),img=self.easyLevelImg,img_hl=self.easyLevelImgHl)
        self.buttonMediumLevel = Button(self.mainSurface,(490,300),(300,90),img=self.mediumLevelImg,img_hl=self.mediumLevelImgHl)
        self.buttonHardLevel = Button(self.mainSurface,(490,400),(300,90),img=self.hardLevelImg,img_hl=self.hardLevelImgHl)

        self.difficultyLvl = 0
        self.difficultySelection = False
        self.easyCurrentLvl = 0
        self.mediumCurrentLvl = 0
        self.hardCurrentLvl = 0
        ## Levels ##
        # Creating objects #

        # Mainloop
        while True:
            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.menu:
                            if not self.difficultySelection:
                                self.buttonStart.buttonStart_clickAction1(self)
                                self.buttonQuit.buttonQuit_clickAction1(self)
                                self.buttonHelp.buttonHelp_clickAction1(self)
                            elif self.difficultySelection:
                                self.buttonEasyLevel.buttonEasyLevel_clickAction1(self)
                                self.buttonMediumLevel.buttonMediumLevel_clickAction1(self)
                                self.buttonHardLevel.buttonHardLevel_clickAction1(self)
                        elif not self.menu:
                            self.level.buttonRun_clickAction1()
                            self.level.buttonMenu_clickAction1()
                            self.level.buttonHelp2_clickAction1()
                        if self.musicToogle:
                            self.buttonMusicOff.buttonMusicOff_clickAction1(self)
                        elif not self.musicToogle:
                            self.buttonMusicOn.buttonMusicOn_clickAction1(self)
                if event.type == pygame.KEYDOWN:
                    if not self.menu:
                        self.level.textBox.typing(event.key)
                        #print(event.key)
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            if not self.menu:
                pressedKeys = pygame.key.get_pressed()
                if(pressedKeys[pygame.K_BACKSPACE]):
                    self.level.textBox.repeating(pygame.K_BACKSPACE)

            self.drawGameWindow()
            pygame.display.flip()
            clock.tick(30)
    def higherLvl(self):
        if(self.difficultyLvl == 0):
            self.easyCurrentLvl = self.easyCurrentLvl + 1
        elif(self.difficultyLvl == 1):
            self.mediumCurrentLvl = self.mediumCurrentLvl + 1
        elif(self.difficultyLvl == 2):
            self.hardCurrentLvl = self.hardCurrentLvl + 1
    def chooseDifficulty(self):
        self.difficultySelection = True
    def newLevel(self):
        cLvl = 0
        if(self.difficultyLvl == 0):
            cLvl = self.easyCurrentLvl
        elif(self.difficultyLvl == 1):
            cLvl = self.mediumCurrentLvl
        elif(self.difficultyLvl == 2):
            cLvl = self.hardCurrentLvl
        self.level = Level(self.mainSurface,cLvl,self.fonts,self,self.difficultyLvl)
        self.helpToogle = False
    def wylaczPomoc(self):
        if self.helpToogle == False:
            self.helpToogle = True
        else:
            self.helpToogle = False
    def drawGameWindow(self):
        self.mainSurface.fill((35,180,220))
        if self.menu:
            self.mainSurface.blit(self.menuBg,(0,0))
            self.buttonStart.drawMe()
            self.buttonQuit.drawMe()
            self.mainSurface.blit(self.textMusic,(0,0))
            self.buttonHelp.drawMe()
            if self.difficultySelection:
                self.mainSurface.blit(self.difficultySelectionImg,(440,100))
                self.buttonEasyLevel.drawMe()
                self.buttonMediumLevel.drawMe()
                self.buttonHardLevel.drawMe()
        else:
            self.level.drawMe()
            if self.level.helpToogle:
                self.mainSurface.blit(self.helpImg, (860, 50))
        if self.helpToogle:
            self.mainSurface.blit(self.helpImg,(860,50))
        if self.musicToogle:
            self.buttonMusicOn.drawMe()
        else:
            self.buttonMusicOff.drawMe()

Game()