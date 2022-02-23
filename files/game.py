import pygame
from files.canvas_obj import object
from files.jumper import jumper
from files.screnemy import enemy

class Game(object):
    def __init__(self) -> None:
        super().__init__()
        pygame.init()
        self.quit = False
        self.enemy = enemy()
        self.player = jumper()
        self.clock = pygame.time.Clock()
        self.menu = True
        self.pause = pygame.Surface((1280,720))
        self.pause = self.pause.convert_alpha()
        self.pause.set_alpha(150)
        self.pause.fill((255,255,255))
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
        
        if self.iscoll(self.x, self.ex,self.y,self.ey):
            self.grspeed = 0
            self.playerc.set_alpha(255)
            # self.quit = True
        if self.y >= 400:
            self.y = 400



    def run(self):
        while not self.quit:
            self.event()
            self.background()
            self.ground()
            self.line()
            self.player.render(self.ind,self.x,self.y)
            self.enemy.render(self.ex,self.ey)
            self.ex -= 10
            self.screen.blit(self.pause,(0,0))
            # self.gravity()
            pygame.display.update()
            self.clock.tick(60)