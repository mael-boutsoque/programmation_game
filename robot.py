from pygame import draw , Rect


class Robot():
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    
    def draw(self,screen):
        draw.rect(screen,(250,0,0),Rect(self.x,self.y,20,20))
    

    ### interaction functions
    def move_rel(self,x,y):
        self.x += x
        self.y += y