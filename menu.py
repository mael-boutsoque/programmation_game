from bloc import Bloc
from pygame import draw , Rect

from bloc_move import Bloc_move
from bloc_none import Bloc_none

class Menu():
    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height
        self.marge = 10
        self.bloc_height = 50
        self.liste = []
        for i in range(10):
            if(i%2==1):
                self.add_bloc(Bloc_none)
            else:
                self.add_bloc(Bloc_move)
    
    def add_bloc(self,bloc:Bloc):
        id = len(self.liste)
        self.liste.append(bloc(self.marge , self.marge*(id+1) + self.bloc_height*id , self.width - 2*self.marge , self.bloc_height ))
    
    def draw(self,screen):
        draw.rect(screen,(255,255,255),Rect(0,0,self.width,self.height))
    
    def draw_blocs(self,screen):
        for bloc in self.liste:
            bloc.draw(screen)
    
    def check_picking(self,mx,my):
        for bloc in self.liste:
            if bloc.pick(mx,my):
                return bloc
        return None
