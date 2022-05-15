import pygame
# from files.menu import Menu
from files.jumper import Player
from files.screnemy import Enemy
from files.canvas_obj import Obj
class Game(Obj):
    def __init__(self) -> None:
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
            if event.type == pygame.KEYDOWN and not self.gover:
                if event.key == pygame.K_ESCAPE and not self.inmenu:
                    # self.quit = True
                    self.grspeed, self.fall = 0,0
                    self.espeed,self.speed = 0,0
                    self.inmenu = True
                    self.fquit()
                if event.key == pygame.K_ESCAPE and self.inmenu:
                    self.fall = 0.2
                    self.grspeed = 3
                    self.speed = 5.8
                    self.espeed = 7
                    self.gover = False
                    self.inmenu = False
                    self.run()
                if event.key == pygame.K_SPACE and not self.start:
                    self.fall = 0.2
                    self.grspeed = 3
                    self.speed = 5.8
                    self.espeed = 7
                    self.gover = False
                    self.inmenu = False
                    self.start = True
                    self.run()
                if event.key == pygame.K_SPACE:
                    self.ind += 2
                if event.key == pygame.K_RIGHT:
                    self.mind += 1
                if event.key == pygame.K_LEFT:
                    self.mind -= 1
                if event.key == pygame.K_RETURN and (self.mind%2) == 0:
                    self.quit = True
                if event.key == pygame.K_RETURN and (self.mind%2) == 1:
                    if self.speed>0:
                        self.fall = 0.2
                        self.grspeed = 3
                        self.espeed = 7
                        self.inmenu = False
                        self.gover = False
                        self.run()
                    else:
                        self.fall = 0.2
                        self.grspeed = 3
                        self.speed = 5.8
                        self.espeed = 7
                        self.inmenu = False
                        self.gover = False
                        self.run()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE: 
                    self.ind = 0
                    self.is_jump = True
    def event(self):
        # Jumping formula 
        self.mx,self.my = pygame.mouse.get_pos()
        self.mouse = pygame.mouse.get_pressed()
        if self.is_jump and not self.gover:
            F = (1/2)*self.mass*(self.speed**2) # Jump/Kinetic energy formula 
            self.y -= F # Moving the player Y 
            self.speed -= self.fall  # slowing speed down
            if self.speed<0:
                self.mass=-1
            if self.y >= 400:
                self.is_jump = False
                self.mass = 1
                self.speed = 5.8
            # pygame.time.delay(10)
        # Collision function
        if self.iscoll(self.x, self.ex,self.y,self.ey) and not self.gover:
            self.gover = True
            self.game_over()
            
        if self.ex <= -90:
            self.ex = 1000
        # Score counting
        if self.ex == self.x-70 and not self.gover:
            self.scorecount += 1
        self.ex -= self.espeed
        if self.hover(350,340,32,96):
            self.Hyes = True
        else:
            self.Hyes = False
        if self.hover(850,340,32,64):
            self.Hno = True
        else:
            self.Hno = False
        if not self.start:
            self.grspeed, self.fall = 0,0
            self.espeed,self.speed = 0,0



    def mouse_detection(self):
        if self.mouse[0] and self.Hyes and not self.gover:
            self.quit = True
        if self.mouse[0] and self.Hno and not self.gover:
            if self.speed>0:
                self.fall = 0.2
                self.grspeed = 3
                self.espeed = 7
                self.inmenu = False
                self.gover = False
                self.run()
            else:
                self.fall = 0.2
                self.grspeed = 3
                self.speed = 5.8
                self.espeed = 7
                self.inmenu = False
                self.gover = False
                self.run()
        if self.mouse[0] and self.Hno and self.gover:
            self.quit = True
        if self.mouse[0] and self.Hyes and self.gover:
            self.grx = 0
            self.Lwidth = 3
            self.x = 350
            self.y = 400
            self.ex = 900
            self.ey = 420
            self.ind = 0
            self.cooldown = 400
            self.speed = 5.8
            self.espeed = 7
            self.mass = 1
            self.scorecount = 0
            self.is_jump = False
            self.grspeed = 3
            self.quit = False
            self.gover = False
            self.inmenu = False
            self.mind = 0
            self.fall = 0.2
            self.start = False
            self.run()
            



    def fquit(self):
        while not self.quit and not self.gover:
            self.screen.blit(self.pause_surf, (0,0))
            self.mouse_detection()
            self.event()
            self.fevent()
            self.textf('Do you want to quit?',360,260,self.color["white"])
            if (self.mind%2) == 0 or self.Hyes:
                self.mind = 0
                self.yescol = self.color["dark_white"]
                self.nocol = self.color["silver"]
            if (self.mind%2) == 1 or self.Hno:
                self.mind = 1
                self.yescol = self.color["silver"]
                self.nocol = self.color["dark_white"]
            self.textf('YES', 350, 340, self.yescol)
            self.textf('NO', 850, 340, self.nocol)
            pygame.display.update()
        # while not self.quit and not self.gover:
        #     self.screen.fill((0,0,0))
        #     self.event()
        #     self.fevent()
        #     self.textf('Do you want to quit? OK No problem ', 360,550)
        #     pygame.display.update( )
    def game_over(self):
        while not self.quit and self.gover:
            self.screen.blit(self.pause_surf,(0,0))
            self.mouse_detection()
            self.event()
            self.fevent()
            self.textf('Do you want to Restart?',320,260,self.color["white"])
            if (self.mind%2) == 0 or self.Hyes:
                self.mind = 0
                self.yescol = self.color["dark_white"]
                self.nocol = self.color["silver"]
            if (self.mind%2) == 1 or self.Hno:
                self.mind = 1
                self.yescol = self.color["silver"]
                self.nocol = self.color["dark_white"]
            self.textf('YES', 350, 340, self.yescol)
            self.textf('NO', 850, 340, self.nocol)
            pygame.display.update()

    def run(self):
        while not self.quit:
            # Event function
            self.fevent()
            self.event()
            # Moving background
            self.background()
            self.ground()
            self.line()
            # Text moving at start
            self.vertlix -= self.grspeed
            if self.vertlix>-850:
                self.high_score()
                self.start_text()
            # Model rendering functions
            self.player.render(self.ind,self.x,self.y)
            self.enemy.render(self.ex,self.ey)
            # Text functions
            self.score()
            # Update and Tick function
            pygame.display.update()
            self.clock.tick(self.FPS)