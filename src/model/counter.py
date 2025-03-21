class Counter:
    def __init__(self):
        self.moves = 0

    def get_moves(self):
        return self.moves

    def inc_moves(self):
        self.moves += 1
