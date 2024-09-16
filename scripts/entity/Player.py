import pygame
from scripts.entity.BaseEntity import BaseEntity

stats = {
    "health": "100",
    "stamina": "100",
    "mana": "100",
    "hunger": "100",
}


class Player(BaseEntity):
    def __init__(self, x, y):
        BaseEntity.__init__(self, x, y, "assets/player.png",
                            (24, 32), "player", 300)
        self.health = stats["health"]
        self.hunger = stats["hunger"]
        self.mana = stats["mana"]
        self.stamina = stats["stamina"]

    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        distance = [0, 0]
        if keys[pygame.K_w]:
            distance[1] = -delta_time
        if keys[pygame.K_s]:
            distance[1] = +delta_time
        if keys[pygame.K_a]:
            distance[0] = -delta_time
        if keys[pygame.K_d]:
            distance[0] = +delta_time
        self.move(distance[0], distance[1])

    def printstats(self):
        print(self.health, self.hunger, self.mana, self.stamina)

    def modifyStats(self, stat, value):
        for x in stats:
            if stat == x:
                stats[x] = value
