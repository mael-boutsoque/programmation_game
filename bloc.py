from pygame import draw , Rect

class Bloc():
    is_picked = False
    def __init__(self,x,y,width,height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (0,255,0)
    
    def draw(self,screen):
        draw.rect(screen , (self.color) , Rect(self.x,self.y,self.width,self.height))
    
    def colide_point(self,x,y):
        self.hitbox = Rect(self.x,self.y,self.width,self.height)
        return self.hitbox.collidepoint(x,y)
    
    def move(self,x,y):
        self.x = x
        self.y = y
    
    def mousing(self,x,y):
        if self.is_picked:
            self.move(x-self.width/2,y-self.height/2)
            return True

        elif self.colide_point(x,y):
            self.is_picked = True
    
    def release(self):
        self.is_picked = False