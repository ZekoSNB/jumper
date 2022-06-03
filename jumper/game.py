import pygame, math, pygame.freetype, json
from jumper.player import Player
from jumper.screnemy import Enemy
class Game:
    def __init__(self) -> None:
        # Initializing the Modules
        pygame.init()
        self.icon = pygame.image.load('assets/images/icon.png')
        self.backgroundload = pygame.image.load('assets/images/background4.png')
        self.groundimg = pygame.image.load('assets/images/ground_full.png')
        self.playerc = pygame.image.load('assets/images/alien1.png')
        self.playerc1 = pygame.image.load('assets/images/alien1_crouch.png')
        self.playerc2 = pygame.image.load('assets/images/alien1_crouch2.png')
        self.playerc = pygame.transform.scale(self.playerc, (100,100))
        self.playerc1 = pygame.transform.scale(self.playerc1, (100,100))
        self.playerc2 = pygame.transform.scale(self.playerc2, (100,100))
        self.groundimg = pygame.transform.scale(self.groundimg, (8000, 280))
        self.pli = [self.playerc,self.playerc1,self.playerc2]
        self.backgroundimg = pygame.transform.scale(self.backgroundload, (1280,520))
        self.WIDTH, self.HEIGHT = 1280,720
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption('Alien Jumper')
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.pyfont = pygame.font.Font('assets/fonts/SPACE.ttf', 32)
        self.spfont = pygame.freetype.Font('assets/fonts/SPACE.ttf', 32)
        self.spfont1 = pygame.freetype.Font('assets/fonts/SPACE.ttf', 28)
        # Variables 
        with open('jumper/JSON/settings.json', 'r') as f:
            self.data = json.load(f)
            f.close()
        self.color = {
            "silver" : 	(170, 170, 170),
            "white"  :  (255,255,255),
            "dark_white": (240,240,240),
            "red"    : (255,0,0),
            "blue"   : (0,0,255),
            "green"  : (0,255,0),
            "light_grey": (30,30,30),
            "black"  : (0,0,0)

        }
        self.grx = 0
        self.Lwidth = 3
        self.ind = 0
        self.mass = 1
        self.scorecount = 0
        self.is_jump = False
        self.grspeed = 3
        self.quit = False
        self.gover = False
        self.inmenu = False
        self.start = False
        self.mind = 0
        self.fall = 0.2
        self.jumpindex = 0
        self.mx,self.my = pygame.mouse.get_pos()
        self.mouse = pygame.mouse.get_pressed()
        self.pause_surf = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.pause_surf.set_alpha(255/10)
        self.pause_surf.fill(self.color["light_grey"])
        self.Hyes,self.Hno = False,False
        self.statex, self.statey, self.statehov = False,False,False
        self.yescol = self.color["silver"]
        self.nocol = self.color["silver"]
        self.FPS = int(self.data['FPS'])
        self.hiscore = int(self.data['HIGHEST'])
        self.hiscorestr = str(f"Highest: {self.hiscore}")
        self.text = self.pyfont.render(self.hiscorestr, True,self.color["white"])
        self.starte = self.pyfont.render("Press       to start the game", True,self.color["white"])
        self.spacete = self.pyfont.render("SPACE", True, self.color["white"],self.color["black"])
        self.clock = pygame.time.Clock()
        # vertical line x = vertlix | vertical line y = vertliy
        self.vertlix,self.vertliy = 240,500
        self.add = 0
        self.listscore = list(str(self.hiscore))
        self.stop_render = -850
        for i in self.listscore:
            self.add += 20
            self.stop_render -= 20
        self.vertlix += self.add
        self.enemy = Enemy(1100,420,self.screen,7)
        self.player = Player(350,400, self.screen,self.pli,5.8)
    def score(self):
        # Render score on the display 
        self.spfont.render_to(self.screen, (0,0), ('Your Score: ' + str(self.scorecount)), self.color["white"])
    def textf(self,text,x,y, color):
        # Rendering any text 
        self.spfont.render_to(self.screen, (x,y), text, color)
    def hover(self,x,y,height,width):
        if self.mx<=(x+width) and self.mx>= x:
            self.statex = True
        else: 
            self.statex = False
        if self.my<=(y+height) and self.my>= y:
            self.statey = True
        else:
            self.statey = False
        if self.statex and self.statey:
            return True
        else: 
            return False
    def high_score(self):
        self.screen.blit(self.text, ((self.vertlix-240-self.add), 532))
    def start_text(self):
        self.screen.blit(self.starte, ((self.vertlix+30), self.vertliy+30))
        self.screen.blit(self.spacete,((self.vertlix+200), (self.vertliy+30)))
    def iscoll(self,x1,x2,y1,y2):
        # Collision function
        x2 -=5
        # Collsion formula
        dis = math.sqrt(math.pow(x2-x1,2)+ math.pow(y2-y1,2))
        if dis>76:
            return False
        if dis<76:
            return True
    def background(self):
        # Background render function
        self.screen.blit(self.backgroundimg, (0,0))
    def ground(self):
        # Ground render and Ground move
        self.grx -= self.grspeed
        self.screen.blit(self.groundimg, (self.grx,500))
        width = 6720
        if self.grx == -width:
            self.screen.blit(self.groundimg, (width+self.grx,500))
            self.grx = 0
    def line(self):
        # Line between background and ground
        pygame.draw.line(self.screen, (255,255,255),(0,500), (1280, 500), self.Lwidth)
        if self.vertlix>-10:
            pygame.draw.line(self.screen, (255,255,255),(self.vertlix,self.vertliy), (self.vertlix, (self.vertliy+220)), self.Lwidth)
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
                    self.enemy.speed,self.player.speed = 0,0
                    self.inmenu = True
                    self.fquit()
                if event.key == pygame.K_ESCAPE and self.inmenu:
                    self.fall = 0.2
                    self.grspeed = 3
                    self.enemy.speed,self.player.speed = 7,5.8
                    self.gover = False
                    self.inmenu = False
                    self.run()
                if event.key == pygame.K_SPACE and not self.start:
                    self.fall = 0.2
                    self.grspeed = 3
                    self.enemy.speed,self.player.speed = 7,5.8
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
                    self.enemy.speed,self.player.speed = 7,5.8
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
            F = (1/2)*self.mass*(self.player.speed**2) # Jump/Kinetic energy formula 
            self.player.y -= F # Moving the player Y 
            self.player.speed -= self.fall  # slowing speed down
            if self.player.speed<0:
                self.mass=-1
            if self.player.y >= 400:
                self.is_jump = False
                self.mass = 1
                self.player.speed = 5.8
        # Collision function
        if self.iscoll(self.player.x, self.enemy.x,self.player.y,self.enemy.y) and not self.gover:
            self.gover = True
            self.game_over()
            
        if self.enemy.x <= -90:
            self.enemy.x = 1100
        # Score counting
        if round(self.enemy.x/10)*10 == self.player.x-70:
            self.scorecount += 1
        self.enemy.x -= self.enemy.speed
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
            self.enemy.speed,self.player.speed = 0,0
        self.vertlix -= self.grspeed



    def mouse_detection(self):
        if self.mouse[0] and self.Hyes and not self.gover:
            self.quit = True
        if self.mouse[0] and self.Hno and not self.gover:
                self.fall = 0.2
                self.grspeed = 3
                self.enemy.speed,self.player.speed = 7,5.8
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
            self.enemy.speed,self.player.speed = 7,5.8
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
            self.player.render(self.ind)
            self.enemy.render()
            # Text functions
            self.score()
            # Update and Tick function
            self.clock.tick(self.FPS)
            pygame.display.update()