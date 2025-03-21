from src.model.entity import Entity


class Creature(Entity):
    def __init__(self, coord, speed, hp):
        super().__init__(coord)
        self.speed = speed
        self.hp = hp

    def make_move(self, new_coord):
        self.move(new_coord)


class Herbivore(Creature):
    def __init__(self, coord, speed, hp):
        super().__init__(coord, speed, hp)

    def is_alive(self):
        return self.hp > 0
    
    def eat_grass(self):
        self.hp += 2

    def __str__(self):
        return "🐮"

    def __repr__(self):
        return "Herbivore"


class Predator(Creature):
    def __init__(self, coord, speed, hp, attack):
        super().__init__(coord, speed, hp)
        self.attack = attack

    def attack_creature(self, creature):
        creature.hp -= self.attack

    def __str__(self):
        return "🐻"

    def __repr__(self):
        return "Predator"
