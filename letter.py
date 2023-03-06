

class Letter:
    def __init__(self, letter=''):
        self.letter = letter
        self.positions = []

    def __repr__(self):
        return f"{self.letter}: {self.positions}"