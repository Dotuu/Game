import pygame

import Tiles

border = Tiles.TileBorder("path", False, True)
grass = Tiles.TileGrass("path", False, False)

map=[
[border,border,border,border,border,border,border,border,border,border],
[border,grass,grass,grass,grass,grass,grass,grass,grass,border],
[border,grass,grass,grass,grass,grass,grass,grass,grass,border],
[border,grass,grass,grass,grass,grass,grass,grass,grass,border],
[border,grass,grass,grass,grass,grass,grass,grass,grass,border],
[border,grass,grass,grass,grass,grass,grass,grass,grass,border],
[border,grass,grass,grass,grass,grass,grass,grass,grass,border],
[border,grass,grass,grass,grass,grass,grass,grass,grass,border],
[border,grass,grass,grass,grass,grass,grass,grass,grass,border],
[border,border,border,border,border,border,border,border,border,border],
]