import random
from src.model.map import Map


class CoordGenerator:
    @staticmethod
    def generate_coords(max_x, max_y, min_x=1, min_y=1):
        x = random.randint(min_x, max_x)
        y = random.randint(min_y, max_y)
        return (x, y)


class BFS:
    @staticmethod
    def find_path(m: Map, start_coord, end_coords: set):
        dxdy = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
        visited = {start_coord: -1}
        queue = [start_coord]
        path = []
        while len(queue) > 0:
            coord = queue.pop(0)
            if coord in end_coords:
                while visited[coord] != -1:
                    path.append(coord)
                    coord = visited[coord]
                    print(coord, end=" ")
                path.append(start_coord)
                break
            for d in dxdy:
                new_coord = (coord[0] + d[0], coord[1] + d[1])
                if (
                    not m.check_coord(new_coord)
                    or new_coord in visited
                    or (m.is_coord_taken(new_coord) and not new_coord in end_coords)
                ):
                    continue
                queue.append(new_coord)
                visited[new_coord] = coord
        return path[::-1]
