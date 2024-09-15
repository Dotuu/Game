import pygame
class Tile:
    def __init__(self, image, isBreakable, hasCollision):
        self.image = pygame.image.load(image)
        self.isBreakable = isBreakable
        self.hasCollision = hasCollision

    def render(self, screen, x, y):
        #pygame.draw.rect(screen, self.color, pygame.Rect(x*64, y*64, (x+1)*64, (y+1)*64))
        screen.blit(self.image, (x*64, y*64))

class TileBorder(Tile):
    def __init__(self):
        Tile.__init__(self,"assets/brick.png",False,True)

class TileGrass(Tile):
    def __init__(self):
        Tile.__init__(self,"assets/grass.png",False,False)
