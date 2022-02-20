import pygame, time
from files.canvas_obj import object
from files.jumper import jumper

class Game(object):
    def __init__(self) -> None:
        super().__init__()
        pygame.init()
        self.quit = False
        self.player = jumper()
        
    #
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit = True
                if event.key == pygame.K_SPACE:
                    self.ind += 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.ind = 0
                    self.is_jump = True
        if self.is_jump:
            F = (1/2)*self.mass*(self.speed**2)
            self.y -= F
            self.speed = self.speed-1
            if self.speed<0:
                self.mass=-1
            if self.speed <= -11:
                self.is_jump = False
                self.mass = 1
                self.speed = 10
        pygame.time.delay(10)
        if self.y >= 400:
            self.y = 400



    def run(self):
        while not self.quit:
            self.event()
            self.background()
            self.ground()
            self.line()
            self.player.render(self.ind,self.x,self.y)
            # self.gravity()
            pygame.display.update()