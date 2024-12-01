import pygame

from map import Map
from menu import Menu
from programm import Programm

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
        self.map = Map(650,0,10,10,100,100)


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

    def draw(self):
        self.win.fill((0,0,0))
        self.menu.draw(self.win)
        self.programm.draw(self.win)
        self.menu.draw_blocs(self.win)
        self.programm.draw_blocs(self.win)
        self.map.draw(self.win)

        pygame.display.flip()

    def events(self):
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                self.running=False
            
            if event.type == pygame.KEYDOWN:
                #print(event)

                if event.key == 32:
                    print("début")
                    self.programm.evolve(self.map,self)