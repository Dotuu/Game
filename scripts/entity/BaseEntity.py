import pygame


class BaseEntity:
    def __init__(self, x, y, sprite, hitbox, type, speed):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(sprite)
        self.hitbox = hitbox
        self.type = type
        self.speed = speed

    def render(self, screen):
        screen.blit(self.sprite, ((self.x - 64) / 2, (self.y - 64) / 2))

    def move(self, distanceX, distanceY):
        self.x += self.speed * distanceX
        self.y += self.speed * distanceY
