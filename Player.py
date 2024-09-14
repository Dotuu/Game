import json

import pygame

import JsonLoader

stats = {
    "health": "100",
    "stamina": "100",
    "mana": "100",
    "hunger": "100",
}

class Player:
    def __init__(self):
        self.health = stats["health"]
        self.hunger = stats["hunger"]
        self.mana = stats["mana"]
        self.stamina = stats["stamina"]
        self.image = pygame.image.load("player.png")

    def printstats(self):
        print(self.health, self.hunger, self.mana, self.stamina)

    def modifyStats(self,stat,value):
        for x in stats:
            if stat == x:
                stats[x] = value
    def render(self,screen,x,y):
        screen.blit(self.image, ((x-64)/2,(y-64)/2))