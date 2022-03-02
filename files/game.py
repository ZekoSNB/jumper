import pygame
from files.canvas_obj import Obj
from files.jumper import Player
from files.screnemy import Enemy

class Game(Obj):
    def __init__(self) -> None:\
        # Passing the Obj __init__ into Game.__init__
        super().__init__()
        # Initializing the Modules
        self.enemy = Enemy()
        self.player = Player()
        # self.menu = True
        # self.pause = pygame.Surface((1280,720))
        # self.pause = self.pause.convert_alpha()
    #
    def event(self):
        # Event Loop for the keys etc.
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
        # Jumping formula 
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
        # Collision function
        if self.iscoll(self.x, self.ex,self.y,self.ey):
            self.grspeed = 0
            self.espeed,self.speed = 0,0
            
        if self.ex <= -90:
            self.ex = 1000
        # Score counting
        if self.ex == self.x-70 :
            self.scorecount += 1
        self.ex -= self.espeed



    def run(self):
        while not self.quit:
            # Event function
            self.event()
            # Moving background
            self.background()
            self.ground()
            self.line()
            # Model rendering functions
            self.player.render(self.ind,self.x,self.y)
            self.enemy.render(self.ex,self.ey)
            # Text functions
            self.score()
            # Update and Tick function
            pygame.display.update()
            self.clock.tick(60)