import pygame
import DrawMap

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.running = False
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)

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
        if keys[pygame.K_w]:
            self.player_pos.y -= 300 * self.delta_time
        if keys[pygame.K_s]:
            self.player_pos.y += 300 * self.delta_time
        if keys[pygame.K_a]:
            self.player_pos.x -= 300 * self.delta_time
        if keys[pygame.K_d]:
            self.player_pos.x += 300 * self.delta_time

    def render(self):
        self.screen.fill("gray")
        DrawMap.renderMap(self.screen)
        pygame.draw.circle(self.screen, "red", self.player_pos, 40)
        pygame.display.flip()

    def quit(self):
        pygame.quit()

if __name__ == "__main__" :
    game = Game()
    game.start()
