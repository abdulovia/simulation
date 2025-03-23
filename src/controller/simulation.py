import random, time
from src.model import Map, Counter
from src.view import Renderer
from src.controller import Actions


class Simulation:
    def __init__(self, l, w):
        self.world_map = Map(l, w)
        self.counter = Counter()
        self.renderer =  Renderer(l, w)
        self.actions = Actions()

    def prepare_simulation(self):
        for action in self.actions.init_actions:
            entity_cnt = random.randint(1, 3)
            while entity_cnt:
                action(self.world_map)
                entity_cnt -= 1

    def next_turn(self):
        for action in self.actions.turn_actions:
            action(self.world_map)

    def run_simulation(self):
        self.prepare_simulation()
        self.renderer.update_and_print_field(self.world_map)
        while True:
            self.next_turn()

            self.counter.inc_moves()
            print(f"{self.counter.get_moves()} move...")

            # print(self.world_map.objects)
            self.renderer.update_and_print_field(self.world_map)
            time.sleep(3)

    def pause_simulation(self):
        pass
