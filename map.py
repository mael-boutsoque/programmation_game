from robot import Robot

from pygame import draw , Rect


class Map():
    def __init__(self , x , y , cwidth , cheight , nb_x , nb_y) -> None:
        self.x = x
        self.y = y
        self.cwidth = cwidth
        self.cheight = cheight
        self.liste = []
        for i in range(nb_x):
            self.liste.append([])
            for y in range(nb_y):
                self.liste[i].append(0)
        
        self.robot_x = 1
        self.robot_y = 1
        self.robot = Robot(x,y)
        self.wait = self.liste[self.robot_x][self.robot_y]
        self.liste[self.robot_x][self.robot_y] = self.robot
    
    def draw(self , screen):
        for i in range(len(self.liste)):
            for j in range(len(self.liste[i])):
                if(self.liste[i][j]==0):
                    draw.rect(screen , (0,250,0) , Rect(self.x + self.cwidth*i , self.y + self.cheight*j , self.cwidth-2 , self.cheight-2))
    
    def move(self,x,y):
        self.liste[self.robot_x][self.robot_y] = self.wait
        self.robot_x , self.robot_y = self.robot_x + x , self.robot_y + y
        
        self.wait = self.liste[self.robot_x][self.robot_y]
        self.liste[self.robot_x][self.robot_y] = self.robot