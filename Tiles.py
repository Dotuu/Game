import pygame
class Tile:
    def __init__(self, color, isBreakable, hasCollision):
        self.color = color
        self.isBreakable = isBreakable
        self.hasCollision = hasCollision

    def render(self, screen, x, y):
        pygame.draw.rect(screen, self.color, pygame.Rect(x*64, y*64, (x+1)*64, (y+1)*64))

class TileBorder(Tile):
    def __init__(self):
        Tile.__init__(self,(111,14,65),False,True)

class TileGrass(Tile):
    def __init__(self):
        Tile.__init__(self,(0,255,0),False,False)