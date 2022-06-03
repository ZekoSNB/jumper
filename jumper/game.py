import pygame
from jumper.player import Player
from jumper.screnemy import Enemy
from jumper.canvas_obj import Obj
class Game(Obj):
    def __init__(self) -> None:
        # Passing the Obj __init__ into Game.__init__
        super().__init__()
        # Initializing the Modules
        self.enemy = Enemy()
        self.player = Player()
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
                if event.key == pygame.K_SPACE and self.jumpindex != 0:
                    self.ind += 2
                if event.key == pygame.K_RIGHT:
                    self.mind += 1
                if event.key == pygame.K_LEFT:
                    self.mind -= 1
                if event.key == pygame.K_RETURN and (self.mind%2) == 0 and self.inmenu:
                    self.quit = True
                if event.key == pygame.K_RETURN and (self.mind%2) == 1 and self.inmenu:
                    self.fall = 0.2
                    self.grspeed = 3
                    self.speed = 5.8
                    self.espeed = 7
                    self.inmenu = False
                    self.gover = False
                    self.run()
            if event.type == pygame.KEYDOWN and self.gover:
                if event.key == pygame.K_RIGHT:
                    self.mind += 1
                if event.key == pygame.K_LEFT:
                    self.mind -= 1
                if event.key == pygame.K_RETURN and (self.mind%2) == 1:
                    self.quit = True
                if event.key == pygame.K_RETURN and (self.mind%2) == 0:
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
                    self.jumpindex = 0
                    self.is_jump = False
                    self.grspeed = 3
                    self.quit = False
                    self.gover = False
                    self.inmenu = False
                    self.mind = 0
                    self.fall = 0.2
                    self.start = False
                    self.vertlix,self.vertliy = 240+self.add,500
                    self.run()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    if self.jumpindex != 0:
                        self.ind = 0
                        self.is_jump = True
                    else: 
                        self.jumpindex=1
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
        # Collision function
        if self.iscoll(self.x, self.ex,self.y,self.ey) and not self.gover:
            self.gover = True
            self.game_over()
            
        if self.ex <= -90:
            self.ex = 1100
        # Score counting
        if round(self.ex/10)*10 == self.x-70:
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
        self.vertlix -= self.grspeed



    def mouse_detection(self):
        if self.mouse[0] and self.Hyes and not self.gover:
            self.quit = True
        if self.mouse[0] and self.Hno and not self.gover:
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
            self.jumpindex = 0
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
            self.vertlix,self.vertliy = 240+self.add,500
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
            if self.vertlix>self.stop_render:
                self.high_score()
                self.start_text()
            # Model rendering functions
            self.player.render(self.ind,self.x,self.y)
            self.enemy.render(self.ex,self.ey)
            # Text functions
            self.score()
            # Update and Tick function
            self.clock.tick(self.FPS)
            pygame.display.update()