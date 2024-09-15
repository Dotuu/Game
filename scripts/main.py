import pygame
import DrawMap
import JsonLoader
from entity.Player import Player


class Game:
    def __init__(self):
        self.settings = JsonLoader.load("settings.json")
        print(self.settings)
        self.screen = pygame.display.set_mode(
            (self.settings["resolution"]["width"], self.settings["resolution"]["height"]))
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.running = False
        self.player = Player(self.screen.get_width() / 2,
                             self.screen.get_height() / 2)
        print((self.screen.get_width() / 2, self.screen.get_height() / 2))

    def start(self):
        pygame.init()
        self.running = True

        while self.running:
            for event in pygame.event.get():
                self.run_event(event)
            self.update()
            self.render()
            self.delta_time = self.clock.tick(60) / 1000

        self.quit()

    def run_event(self, event: pygame.Event):
        if event.type == pygame.QUIT:
            self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        distance = [0, 0]
        if keys[pygame.K_w]:
            distance[1] = -self.delta_time
        if keys[pygame.K_s]:
            distance[1] = +self.delta_time
        if keys[pygame.K_a]:
            distance[0] = -self.delta_time
        if keys[pygame.K_d]:
            distance[0] = +self.delta_time
        self.player.move(distance[0], distance[1])

    def render(self):
        self.screen.fill("gray")
        DrawMap.renderMap(self.screen)
        self.player.render(self.screen)
        pygame.display.flip()

    def quit(self):
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.start()
