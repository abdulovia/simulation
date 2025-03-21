from src.model.point import Point


class Entity:
    def __init__(self, coord):
        self.point = Point(coord)

    def move(self, new_coord):
        self.point = Point(new_coord)
