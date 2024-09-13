import pygame
class Tile:
    def __init__(self, texture, isBreakable, hasCollision):
        self.texture = texture
        self.isBreakable = isBreakable
        self.hasCollision = hasCollision

    def render(self, screen, x, y):
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x*64, y*64, (x+1)*64, (y+1)*64))

class TileBorder(Tile):
    def __init__(self):
        Tile.__init__(self,"filepath",False,True)

class TileGrass(Tile):
    def __init__(self):
        Tile.__init__(self,"filepath",False,False)