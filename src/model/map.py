class Map:
    objects = {}
    taken_coords = dict()

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def add_entity(self, entityObj):
        if repr(entityObj) not in self.objects:
            self.objects[repr(entityObj)] = [entityObj]
        else:
            self.objects[repr(entityObj)].append(entityObj)
        coordinate = entityObj.point.coord
        self.taken_coords[coordinate] = True

    def remove_entity(self, entityObj):
        self.objects[repr(entityObj)].remove(entityObj)
        coordinate = entityObj.point.coord
        self.taken_coords[coordinate] = False

    def get_entities(self, entityType):
        return self.objects[entityType]

    def get_entity(self, coord, entityType):
        entities = self.objects[entityType]
        for entity in entities:
            if entity.point.coord == coord:
                return entity
        return None

    def is_coord_taken(self, coord) -> bool:
        if coord in self.taken_coords:
            return self.taken_coords[coord]
        return False

    def check_coord(self, coord) -> bool:
        if coord[0] < 1 or coord[1] < 1 or coord[0] > self.length or coord[1] > self.width:
            return False
        return True

    def get_entities_coords(self, entityType):
        entities = self.objects[entityType]
        coords = set()
        for entity in entities:
            coords.add(entity.point.coord)
        return coords
