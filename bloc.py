from pygame import draw , Rect

class Bloc():
    def __init__(self,x,y,width,height,color) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    def draw(self,screen):
        draw.rect(screen , (self.color) , Rect(self.x,self.y,self.width,self.height))