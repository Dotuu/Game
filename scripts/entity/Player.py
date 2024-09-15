import pygame
from entity.BaseEntity import BaseEntity

stats = {
    "health": "100",
    "stamina": "100",
    "mana": "100",
    "hunger": "100",
}


class Player(BaseEntity):
    def __init__(self, x, y):
        BaseEntity.__init__(self, x, y, "assets/player.png", (), "player", 300)
        self.health = stats["health"]
        self.hunger = stats["hunger"]
        self.mana = stats["mana"]
        self.stamina = stats["stamina"]

    def printstats(self):
        print(self.health, self.hunger, self.mana, self.stamina)

    def modifyStats(self, stat, value):
        for x in stats:
            if stat == x:
                stats[x] = value
