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
        if bloc.x>self.x and bloc.x+bloc.width<self.x+self.width:
            id = (bloc.y+self.marge)//self.bloc_height
            if(id>len(self.liste)):
                print("ajout du bloc")
                bloc.move(self.x+self.marge,len(self.liste)*(self.bloc_height+self.marge)+self.marge)
                self.liste.append(bloc)
            else:
                print("implementer la fonction pour decaler les blocs")
            return True
        else:
            return False
    
    def remove(self,bloc:Bloc):
        if bloc in self.liste:
            self.liste.pop(self.liste.index(bloc))
            self.move_ups()
    
    def move_ups(self):
        for i in range(1,len(self.liste)):
            self.liste[i].move(self.x+self.marge,i*(self.bloc_height+self.marge)+self.marge)
    
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