class mapElement(object):
    def __init__(self,map,gridPos,pixSize,bodyImage):
        self.surface = map.surface
        self.map = map
        self.gridPos = gridPos
        self.pixSize = pixSize
        self.bodyImage = bodyImage

    def drawMe(self, pixPos):
        self.surface.blit(self.bodyImage,pixPos)