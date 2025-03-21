class Point(object):
    def __init__(self, coord: tuple):
        self.coord = coord

    def __str__(self):
        return f"Point({self.coord[0]}, {self.coord[1]})"
