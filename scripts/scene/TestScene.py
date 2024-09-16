from scripts import DrawMap
from scripts.entity.Player import Player
from scripts.scene.BaseScene import BaseScene


class TestScene(BaseScene):
    def __init__(self, screen):
        super().__init__("TestScene")
        self.screen = screen
        self.player = Player(self.screen.get_width() / 2,
                             self.screen.get_height() / 2)
        self.objects.append(self.player)

    def render(self, screen):
        DrawMap.renderMap(screen)
        super().render(screen)
