import pygame, math, pygame.freetype, json

class Obj:
    def __init__(self) -> None:
        pygame.init()
        # Loading Images and Fonts into the game
        self.icon = pygame.image.load('assets/images/icon.png')
        self.backgroundload = pygame.image.load('assets/images/background3.png')
        self.groundimg = pygame.image.load('assets/images/ground_full.png')
        self.playerc = pygame.image.load('assets/images/alien1.png')
        self.playerc1 = pygame.image.load('assets/images/alien1_crouch.png')
        self.playerc2 = pygame.image.load('assets/images/alien1_crouch2.png')
        self.enemyimg = pygame.image.load('assets/images/enemy1.png')
        self.enemyimg = pygame.transform.scale(self.enemyimg, (80,80))
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
        with open('files/JSON/settings.json', 'r') as f:
            self.data = json.load(f)
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
        self.x = 350
        self.y = 400
        self.ex = 1100
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
        self.start = False
        self.mind = 0
        self.fall = 0.2
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
        self.vertlix,self.vertliy = 250,500
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
    def iscoll(self,x1,x2,y1,y2):
        # Collision function
        x2 -=5
        # Collsion formula
        dis = math.sqrt(math.pow(x2-x1,2)+ math.pow(y2-y1,2))
        if dis>76:
            return False
        if dis<76:
            return True
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
        # self.spfont.render_to(self.screen, ((self.vertlix-250),(self.vertliy)), self.hiscorestr,self.color["white"])
        self.screen.blit(self.text, (self.vertlix-250, self.vertliy+32))
    def start_text(self):
        self.screen.blit(self.starte, ((self.vertlix+30), self.vertliy+30))
        self.screen.blit(self.spacete,((self.vertlix+200), (self.vertliy+30)))