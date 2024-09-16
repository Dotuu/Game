class Skills:
    def __init__(self):
        self.xp = 0
        self.xpToLevelUp = 0
        self.level = 1

    def gain_skill(self, gained):
        self.xp += gained


class Mining(Skills):
    def __init__(self):
        Skills.__init__(self)


class Woodcutting(Skills):
    def __init__(self):
        Skills.__init__(self)


class Fishing(Skills):
    def __init__(self):
        Skills.__init__(self)


class Smithing(Skills):
    def __init__(self):
        Skills.__init__(self)


class Archery(Skills):
    def __init__(self):
        Skills.__init__(self)


class Magic(Skills):
    def __init__(self):
        Skills.__init__(self)


class Melee(Skills):
    def __init__(self):
        Skills.__init__(self)
