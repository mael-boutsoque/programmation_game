from bloc import Bloc


class Bloc_move(Bloc):
    def __init__(self, x, y, width, height) -> None:
        super().__init__(x, y, width, height)
        self.color0 = (0,0,100)
        self.color = self.color0
    
    def evole(self, id , map):
        print("move")
        map.move(0,1)

        #next
        return id+1


class Bloc_none(Bloc):
    def __init__(self, x, y, width, height) -> None:
        super().__init__(x, y, width, height)
        self.color0 = (100,0,0)
        self.color = self.color0
    
    def evole(self, id , map):
        print("none")

        #next
        return id+1