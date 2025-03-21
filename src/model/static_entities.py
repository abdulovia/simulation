from src.model.entity import Entity


class Grass(Entity):
    def __init__(self, coord):
        super().__init__(coord)

    def __str__(self):
        return "🌺"

    def __repr__(self):
        return "Grass"


class Rock(Entity):
    def __init__(self, coord):
        super().__init__(coord)

    def __str__(self):
        return "🐚"

    def __repr__(self):
        return "Rock"


class Tree(Entity):
    def __init__(self, coord):
        super().__init__(coord)

    def __str__(self):
        return "🌳"

    def __repr__(self):
        return "Tree"
