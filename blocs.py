from bloc import Bloc
from pygame import draw , Rect


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


class Bloc_loop(Bloc):
    def __init__(self, x, y, width, height) -> None:
        super().__init__(x, y, width, height)
        self.color0 = (100,0,0)
        self.color = self.color0
        self.destination = Bloc_none(self.x,self.y+self.height + 10,width,height)
    
    def evole(self, id , map):
        print("none")

        #next
        return id+1
    
    def release(self, programm):
         super().release(programm)
         programm.remove(self.destination)
         programm.add_bloc(self.destination)
    
    
    def move_center(self,x,y):
        super().move_center(x,y)
        self.destination.move_center(self.x , self.y+self.height + 10)
    
    def move(self,x,y):
        super().move(x,y)
        self.destination.move(self.x,self.y+self.height + 10)
    
    def draw(self,screen):
        super().draw(screen)
        
        draw.rect(screen , (self.color) , Rect(self.destination.x , self.destination.y , self.destination.width , self.destination.height))
        screen.blit(self.font.render(self.__class__.__name__,True,(255,255,255)) , (self.destination.x , self.destination.y))