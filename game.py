import pygame

class Game():
    def __init__(self) -> None:
        self.running = True
        pygame.init()
        pygame.font.init()
        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.win = pygame.display.set_mode((1920/2,1080/2))

        self.start()
    
    def start(self):
        self.loop()
    
    def loop(self):
        while self.running:
            self.events()
            self.draw()
            pygame.display.flip()

    def draw(self):
        self.win.fill((0,0,0))

    def events(self):
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                self.running=False