import pygame

from menu import Menu
from programm import Programm
from robot import Robot

class Game():
    is_draging = False
    moving_bloc = None
    def __init__(self) -> None:
        width = 1920
        height = 1080
        self.width = width/2
        self.height = height/2
        self.running = True
        pygame.init()
        pygame.font.init()
        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.win = pygame.display.set_mode((self.width,self.height))

        #assets
        self.menu = Menu(300 , self.height)
        self.programm = Programm(320 , 300 , self.height)
        self.robot = Robot(700,300)


        #start game
        self.loop()

    
    def loop(self):
        while self.running:
            #moving blocs
            mx,my = pygame.mouse.get_pos()
            m_is_clicked = pygame.mouse.get_pressed()[0]


            if self.moving_bloc is None and m_is_clicked:
                self.moving_bloc = self.menu.check_picking(mx,my)
            elif not self.moving_bloc is None and not m_is_clicked:
                self.moving_bloc.release(self.programm)
                self.moving_bloc = None

            if not self.moving_bloc is None:
                self.moving_bloc.move_center(mx,my)




            self.events()
            self.draw()
            pygame.display.flip()

    def draw(self):
        self.win.fill((0,0,0))
        self.menu.draw(self.win)
        self.programm.draw(self.win)
        self.menu.draw_blocs(self.win)
        self.programm.draw_blocs(self.win)
        self.robot.draw(self.win)

    def events(self):
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                self.running=False