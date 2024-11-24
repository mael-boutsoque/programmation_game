from bloc import Bloc


class Menu():
    def __init__(self) -> None:
        self.liste = [Bloc(10,10,100,100)]
    
    def draw(self,screen):
        for bloc in self.liste:
            bloc.draw(screen)