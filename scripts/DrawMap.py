import pygame

import Tiles

border = Tiles.TileBorder()
grass = Tiles.TileGrass()

map = [
    [border, border, border, border, border,
        border, border, border, border, border],
    [border, grass, grass, grass, grass, grass, grass, grass, grass, border],
    [border, grass, grass, grass, grass, grass, grass, grass, grass, border],
    [border, grass, grass, grass, grass, grass, grass, grass, grass, border],
    [border, grass, grass, grass, grass, grass, grass, grass, grass, border],
    [border, grass, grass, grass, grass, grass, grass, grass, grass, border],
    [border, grass, grass, grass, grass, grass, grass, grass, grass, border],
    [border, grass, grass, grass, grass, grass, grass, grass, grass, border],
    [border, grass, grass, grass, grass, grass, grass, grass, grass, border],
    [border, border, border, border, border,
        border, border, border, border, border],
]


def renderMap(screen):
    for y in range(len(map)):
        for x in range(len(map[y])):
            tile = map[y][x]
            tile.render(screen, x, y)
