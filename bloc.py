from pygame import draw , Rect


class Bloc():
    def __init__(self,x,y,width,height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color0 = (0,100,0)
        self.color = self.color0
    
    def draw(self,screen):
        draw.rect(screen , (self.color) , Rect(self.x,self.y,self.width,self.height))
    
    def colide_point(self,x,y):
        self.hitbox = Rect(self.x,self.y,self.width,self.height)
        return self.hitbox.collidepoint(x,y)
    
    def move(self,x,y):
        self.x = x
        self.y = y
    
    def move_center(self,x,y):
        self.x = x-self.width/2
        self.y = y-self.height/2
    
    def pick(self,x,y):
        if self.colide_point(x,y):
            return True
        else:
            return False
    
    def release(self,programm):
        print("bloc dropped")
        programm.remove(self)
        programm.add_bloc(self)
    
    def __str__(self) -> str:
        return f"[bloc({self.x},{self.y})]"

    def evole(self,robot):
        raise NotImplementedError
    
    def higtlight(self):
        self.color = (max(self.color0[0]+50,250),max(self.color0[1]+50,250),max(self.color0[2]+50,250))
    def unhightlight(self):
        self.color = self.color0
