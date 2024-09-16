class BaseScene:
    def __init__(self, name):
        self.name = name
        self.objects = []

    def update(self, delta_time):
        for object in self.objects:
            object.update(delta_time)

    def render(self, screen):
        for object in self.objects:
            object.render(screen)
