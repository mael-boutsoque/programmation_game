from bloc import Bloc
from pygame import draw , Rect


class Programm():
    def __init__(self,x,width,height) -> None:
        self.x = x
        self.width = width
        self.height = height
        self.marge = 10
        self.bloc_height = 50
        self.liste = []
    
    def add_bloc(self,bloc:Bloc):
        #self.liste.append(bloc)
        pass
    
    def draw(self,screen):
        draw.rect(screen,(255,255,255),Rect(self.x,0,self.width,self.height))
    
    def draw_blocs(self,screen):
        for bloc in self.liste:
            bloc.draw(screen)
    
    def evolve(self,mousex,mousey,mouse_is_clicked):
        for bloc in self.liste:
            if mouse_is_clicked:
                if bloc.mousing(mousex,mousey):
                    return True
            elif bloc.is_picked :
                bloc.release()
                return False