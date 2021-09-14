import pygame
import time

myKeyboard = {
    32: " ",
    48: "0",
    49: "1",
    50: "2",
    51: "3",
    52: "4",
    53: "5",
    54: "6",
    55: "7",
    56: "8",
    57: "9",
    59: ";",
    97: "a",
    98: "b",
    99: "c",
    100: "d",
    101: "e",
    102: "f",
    103: "g",
    104: "h",
    105: "i",
    106: "j",
    107: "k",
    108: "l",
    109: "m",
    110: "n",
    111: "o",
    112: "p",
    113: "q",
    114: "r",
    115: "s",
    116: "t",
    117: "u",
    118: "v",
    119: "w",
    120: "x",
    121: "y",
    122: "z"
}
commands = ["obroc w lewo;",
            "obroc w prawo;",
            "idz w lewo;",
            "idz w prawo;",
            "idz w gore;",
            "idz w dol;",
            "times;",
            "otworz skrzynie;",
            "wez skarb;"]

class TextBox(object):
    def __init__(self,level,surface,pixSize,fgColor,bColor,textColor,font,game):
        self.game = game
        self.level = level
        self.surface = surface
        self.pixSize = pixSize
        self.fgColor = fgColor
        self.bColor = bColor
        self.lines = []
        self.lines.append("")
        self.currentLine = 0
        self.textColor = textColor
        self.font = font

    def drawMe(self, pixPos):
        pygame.draw.rect(self.surface,(43,43,43),(pixPos[0],pixPos[1],self.pixSize[0],self.pixSize[1]),0)
        pygame.draw.rect(self.surface,self.bColor,(pixPos[0],pixPos[1],self.pixSize[0],self.pixSize[1]),1)
        i=0
        for line in self.lines:
            font = pygame.font.SysFont('arial', 18)
            if i == self.currentLine:
                number = font.render(str(i), 1, (160,159,159))
                pygame.draw.rect(self.surface,(0,0,0),(pixPos[0]+1,pixPos[1]+1+i*30,24,30))
                self.surface.blit(number,(pixPos[0]+(24/2)-(number.get_width()/2)+1,pixPos[1]+(30/2)-(number.get_height()/2)+1+i*30))
            else:
                number = font.render(str(i), 1, (96,99,102))
                pygame.draw.rect(self.surface,(49,51,53),(pixPos[0]+1,pixPos[1]+1+i*30,24,30))
                self.surface.blit(number,(pixPos[0]+(24/2)-(number.get_width()/2)+1,pixPos[1]+(30/2)-(number.get_height()/2)+1+i*30))
            i+=1
        i=0
        for line in self.lines:
            text = self.font.render(str(line), 1, (169,183,198))
            self.surface.blit(text, (870 + 8, 40 + i * 30))
            i+=1

    def repeating(self, eventKey):
        if eventKey == 8:
            if self.lines[self.currentLine] == "":
                if self.currentLine != 0:
                    del self.lines[self.currentLine]
                    self.currentLine -= 1
            elif not self.lines[self.currentLine] == "":
                self.lines[self.currentLine] = self.lines[self.currentLine][:-1]
        time.sleep(0.15)
    def typing(self,eventKey):
        if eventKey == 13 or eventKey == 271:
            self.lines.append("")
            self.currentLine += 1
        elif eventKey == 273 or eventKey == 264:
            if self.currentLine != 0:
                self.currentLine -= 1
        elif eventKey == 274 or eventKey == 258:
            if self.currentLine < len(self.lines)-1:
                self.currentLine += 1
        elif eventKey != 8:
            if eventKey in myKeyboard:
                self.lines[self.currentLine] += (myKeyboard[eventKey])
        #print(self.lines)
        #print(self.currentLine)
    def analizeCode(self,map,player):
        for line in self.lines:
            #pygame.time.delay(1000)
            if line in commands and line[-1] == ';':
                #pygame.time.delay(1000)
                if line == "obroc w lewo;":
                    player.turnLeft()
                elif line == "obroc w prawo;":
                    player.turnRight()
                elif line == "idz w lewo;":
                    try:
                        player.turnLeft()
                        player.goLeft()
                    except Exception:
                        break
                elif line == "idz w prawo;":
                    try:
                        player.turnRight()
                        player.goRight()
                    except Exception:
                        break
                elif line == "idz w gore;":
                    try:
                        player.goUp()
                    except Exception:
                        break
                elif line == "idz w dol;":
                    try:
                        player.goDown()
                    except Exception:
                        break
                elif line == "otworz skrzynie;":
                    nearLeftGridPos = (player.gridPos[0]-1,player.gridPos[1])
                    if nearLeftGridPos == self.level.map.treasure.gridPos:
                        self.level.map.treasure.closed = False
                    nearRightGridPos = (player.gridPos[0] + 1, player.gridPos[1])
                    if nearRightGridPos == self.level.map.treasure.gridPos:
                        self.level.map.treasure.closed = False
                    nearUpGridPos = (player.gridPos[0],player.gridPos[1]-1)
                    if nearUpGridPos == self.level.map.treasure.gridPos:
                        self.level.map.treasure.closed = False
                    nearDownGridPos = (player.gridPos[0], player.gridPos[1]+1)
                    if nearDownGridPos == self.level.map.treasure.gridPos:
                        self.level.map.treasure.closed = False
                elif line == "wez skarb;":
                    nearLeftGridPos = (player.gridPos[0]-1,player.gridPos[1])
                    if nearLeftGridPos == self.level.map.treasure.gridPos and self.level.map.treasure.closed == False:
                        self.level.map.treasure.playerGot = True
                        self.game.higherLvl()
                        self.game.newLevel()
                    nearRightGridPos = (player.gridPos[0]+1, player.gridPos[1])
                    if nearRightGridPos == self.level.map.treasure.gridPos and self.level.map.treasure.closed == False:
                        map.gridElements[self.level.map.treasure.gridPos[0]][self.level.map.treasure.gridPos[1]] = []
                        self.level.map.treasure.playerGot = True
                        self.game.higherLvl()
                        self.game.newLevel()
                    nearUpGridPos = (player.gridPos[0],player.gridPos[1]-1)
                    if nearUpGridPos == self.level.map.treasure.gridPos and self.level.map.treasure.closed == False:
                        self.level.map.treasure.playerGot = True
                        self.game.higherLvl()
                        self.game.newLevel()
                    nearDownGridPos = (player.gridPos[0], player.gridPos[1]+1)
                    if nearDownGridPos == self.level.map.treasure.gridPos and self.level.map.treasure.closed == False:
                        map.gridElements[self.level.map.treasure.gridPos[0]][self.level.map.treasure.gridPos[1]] = []
                        self.level.map.treasure.playerGot = True
                        self.game.higherLvl()
                        self.game.newLevel()

                map.drawMe()
                pygame.display.flip()
            elif "razy;" in line:
                x = findNumber(line)
                if line == "idz w lewo " + str(x) + " razy;":
                    if player.gridPos[0] - x >= 0:
                        player.turnLeft()
                        for j in range(x):
                            pygame.time.delay(1000)
                            player.goLeft()
                            map.drawMe()
                            pygame.display.flip()
                elif line == "idz w prawo " + str(x) + " razy;":
                    if player.gridPos[0] + x <= 15:
                        player.turnRight()
                        for j in range(x):
                            pygame.time.delay(1000)
                            player.goRight()
                            map.drawMe()
                            pygame.display.flip()
                elif line == "idz w gore " + str(x) + " razy;":
                    if player.gridPos[1] - x >= 0:
                        for j in range(x):
                            pygame.time.delay(1000)
                            player.goUp()
                            map.drawMe()
                            pygame.display.flip()
                elif line == "idz w dol " + str(x) + " razy;":
                    if player.gridPos[1] + x <= 11:
                        for j in range(x):
                            pygame.time.delay(1000)
                            player.goDown()
                            map.drawMe()
                            pygame.display.flip()
            pygame.time.delay(1000)
        if(self.level.map.treasure.playerGot == False):
            player.resetPosition()
            self.level.map.treasure.closed = True

def findNumber(line):
    numbers = [int(s) for s in line.split() if s.isdigit()]
    return numbers[0]
def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')
