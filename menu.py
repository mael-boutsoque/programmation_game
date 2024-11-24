from bloc import Bloc
from pygame import draw , Rect


class Menu():
    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height
        self.marge = 10
        self.liste = []
        self.add_bloc(Bloc)
    
    def add_bloc(self,bloc:Bloc):
        id = len(self.liste)+1
        self.liste.append(bloc(self.marge , self.marge*id , self.width - 2*self.marge , 50))
    
    def draw(self,screen):
        draw.rect(screen,(255,255,255),Rect(0,0,self.width,self.height))
        for bloc in self.liste:
            bloc.draw(screen)