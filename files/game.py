import pygame
# from files.menu import Menu
from files.jumper import Player
from files.screnemy import Enemy
from files.canvas_obj import Obj
class Game(Obj):
    def __init__(self) -> None:\
        # Passing the Obj __init__ into Game.__init__
        super().__init__()
        # Initializing the Modules
        self.enemy = Enemy()
        self.player = Player()
        # self.menu = Menu()
        # self.menu = True
        # self.pause = pygame.Surface((1280,720))
        # self.pause = self.pause.convert_alpha()
    # even function to check user input
    def fevent(self):
        # Event Loop for the keys etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # self.quit = True
                    self.menu.start()
                if event.key == pygame.K_SPACE:
                    self.ind += 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.ind = 0
                    self.is_jump = True
    def event(self):
        # Jumping formula 
        if self.is_jump and not self.iscoll(self.x, self.ex,self.y,self.ey):
            F = (1/2)*self.mass*(self.speed**2) # Jump/Kinetic energy formula 
            self.y -= F # Moving the player Y 
            self.speed -= 0.2 # slowing speed down
            if self.speed<0:
                self.mass=-1
            if self.y >= 400:
                self.is_jump = False
                self.mass = 1
                self.speed = 5.8
            # pygame.time.delay(10)
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

    def menu(self):
        while not self.quit:
            self.event

    def run(self):
        while not self.quit:
            # Event function
            self.fevent()
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
            print(self.clock.get_fps())
            self.clock.tick(self.FPS)