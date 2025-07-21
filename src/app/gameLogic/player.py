

class Player:
    def __init__(self, id=-1, start=None):
        self.id = id
        self.square = start
        self.chips = [False, False, False, False]