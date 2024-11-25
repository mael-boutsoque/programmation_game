from bloc import Bloc


class Bloc_none(Bloc):
    def __init__(self, x, y, width, height) -> None:
        super().__init__(x, y, width, height)
        self.color0 = (100,0,0)
        self.color = self.color0
    
    def evole(self, id , robot):
        print("none")

        #next
        return id+1