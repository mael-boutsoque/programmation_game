from bloc import Bloc


class Bloc_move(Bloc):
    def __init__(self, x, y, width, height) -> None:
        super().__init__(x, y, width, height)
        self.color = (0,0,250)