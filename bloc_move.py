from bloc import Bloc


class Bloc_move(Bloc):
    def __init__(self, x, y, width, height) -> None:
        super().__init__(x, y, width, height)
        self.color0 = (0,0,100)
        self.color = self.color0
    
    def evole(self, id , robot):
        print("move")
        robot.move_rel(0,100)

        #next
        return id+1