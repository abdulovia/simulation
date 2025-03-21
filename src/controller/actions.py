import random
from src.model.map import Map
import src.controller.utils as utils
import src.model.static_entities as static_entities
import src.model.dynamic_entities as dynamic_entities


class Actions:
    def __init__(self):
        self.init_actions = [
            StaticEntityCreator.create_grass,
            StaticEntityCreator.create_rock,
            StaticEntityCreator.create_tree,
            DynamicEntityCreator.create_herbivore,
            DynamicEntityCreator.create_predator,
        ]
        self.turn_actions = [
            CreatureMover.move_all,
            GrassAdder.add_grass,
            HerbivoreAdder.add_herbivore,
        ]


class EntityCreator:
    @staticmethod
    def create_entity(m: Map, entity, *args):
        for _ in range(100):
            coord = utils.CoordGenerator.generate_coords(m.length, m.width)
            if not m.is_coord_taken(coord):
                m.add_entity(entity(coord, *args))
                print(f"log: {entity} with args {list(args)} placed at {coord}")
                return
        print(f"log: {entity} could not be created: not enough space on the map!")


class StaticEntityCreator:
    @staticmethod
    def create_grass(m: Map):
        EntityCreator.create_entity(m, static_entities.Grass)

    @staticmethod
    def create_rock(m: Map):
        EntityCreator.create_entity(m, static_entities.Rock)

    @staticmethod
    def create_tree(m: Map):
        EntityCreator.create_entity(m, static_entities.Tree)


class DynamicEntityCreator:
    @staticmethod
    def create_herbivore(m: Map):
        speed = random.randint(1, 6)
        hp = random.randint(5, 15)
        EntityCreator.create_entity(m, dynamic_entities.Herbivore, speed, hp)

    @staticmethod
    def create_predator(m: Map):
        speed = random.randint(1, 6)
        hp = random.randint(1, 10)
        attack = random.randint(1, 3)
        EntityCreator.create_entity(
            m, dynamic_entities.Predator, speed, hp, attack
        )


class CreatureMover:
    @staticmethod
    def move_all(m: Map):
        herbivores = m.objects["Herbivore"].copy()
        predators = m.objects["Predator"].copy()
        for herbivore in herbivores:
            CreatureMover.move_herbivore(m, herbivore)
        for predator in predators:
            CreatureMover.move_predator(m, predator)

    @staticmethod
    def move_herbivore(m: Map, herbivore: dynamic_entities.Herbivore):
        grass_coords = m.get_entities_coords("Grass")
        path = utils.BFS.find_path(m, herbivore.point.coord, grass_coords)
        m.remove_entity(herbivore)
        if len(path) <= 1:
            print("No grass left to eat")
        elif len(path) == 2:
            grass = m.get_entity(path[-1], "Grass")
            herbivore.eat_grass()
            m.remove_entity(grass)
            print(f"Herbivore {herbivore.point} ate grass at {path[-1]}")
            herbivore.make_move(path[-1]) # place at grass cell
        elif herbivore.speed >= len(path) - 1:
            print(f"Herbivore {herbivore.point} walked to grass {path[-2]}")
            herbivore.make_move(path[-2]) # the closest cell to grass
        else:
            print(f"Herbivore {herbivore.point} to {path[herbivore.speed]}")
            herbivore.make_move(path[herbivore.speed])
        m.add_entity(herbivore)

    @staticmethod
    def move_predator(m: Map, predator: dynamic_entities.Predator):
        herbivore_coords = m.get_entities_coords("Herbivore")
        path = utils.BFS.find_path(m, predator.point.coord, herbivore_coords)
        m.remove_entity(predator)
        if len(path) <= 1:
            print("No herbivores left to attack")
        elif len(path) == 2:
            herbivore = m.get_entity(path[-1], "Herbivore")
            predator.attack_creature(herbivore)
            print(f"Predator {predator.point} attacked herbivore at {path[-1]}")
            if not herbivore.is_alive():
                print(f"Herbivore {herbivore.point} died")
                m.remove_entity(herbivore)
        elif predator.speed >= len(path) - 1:
            print(f"Predator {predator.point} close to herbivore {path[-2]}")
            predator.make_move(path[-2])
        else:
            print(f"Predator {predator.point} to {path[predator.speed]}")
            predator.make_move(path[predator.speed])
        m.add_entity(predator)


class GrassAdder:
    @staticmethod
    def add_grass(m: Map):
        entities = m.get_entities("Grass")
        if len(entities) == 0:
            grass_cnt = random.randint(1, 3)
            while grass_cnt:
                StaticEntityCreator.create_grass(m)
                grass_cnt -= 1

class HerbivoreAdder:
    @staticmethod
    def add_herbivore(m: Map):
        entities = m.get_entities("Herbivore")
        if len(entities) == 0:
            herb_cnt = random.randint(1, 2)
            while herb_cnt:
                DynamicEntityCreator.create_herbivore(m)
                herb_cnt -= 1
