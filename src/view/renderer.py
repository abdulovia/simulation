class Renderer:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.field = [["🌱" for _ in range(width)] for _ in range(length)]

    def update_and_print_field(self, world_map):
        self.field = [["🌱" for _ in range(self.width)] for _ in range(self.length)]
        for entity_list in world_map.objects.values():
            for entity in entity_list:
                X = entity.point.coord[0] - 1
                Y = entity.point.coord[1] - 1
                self.field[X][Y] = str(entity)
        self.print_field()

    def print_field(self):
        for i in range(self.length):
            for j in range(self.width):
                print(self.field[i][j], end=" ")
            print()
        print()
