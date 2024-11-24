import pygame

from menu import Menu

class Game():
    is_draging = False
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

        self.start()
    
    def start(self):
        self.loop()
    
    def loop(self):
        while self.running:
            #moving blocs
            mx,my = pygame.mouse.get_pos()
            m_is_clicked = pygame.mouse.get_pressed()[0]
            self.is_draging = self.menu.evolve(mx,my,m_is_clicked)




            self.events()
            self.draw()
            pygame.display.flip()

    def draw(self):
        self.win.fill((0,0,0))
        self.menu.draw(self.win)

    def events(self):
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                self.running=False