import pygame

from scripts import JsonLoader
from scripts.scene.TestScene import TestScene


class Game:
    def __init__(self):
        self.settings = JsonLoader.load("settings.json")
        self.screen = pygame.display.set_mode(
            (self.settings["resolution"]["width"], self.settings["resolution"]["height"]))
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.running = False
        self.scenes = [TestScene(self.screen)]

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
        for scene in self.scenes:
            scene.update(self.delta_time)

    def render(self):
        self.screen.fill("black")
        for scene in self.scenes:
            scene.render(self.screen)
        pygame.display.flip()

    def quit(self):
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.start()
