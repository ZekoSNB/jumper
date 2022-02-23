import pygame, math



class object:
    def __init__(self) -> None:
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
        self.grx = 0
        self.Lwidth = 3
        self.x = 150
        self.y = 400
        self.ex = 900
        self.ey = 420
        self.ind = 0
        self.last = pygame.time.get_ticks()
        self.cooldown = 400
        self.speed = 10
        self.mass = 1
        self.is_jump = False
        self.grspeed = 3
    def background(self):
        self.screen.blit(self.backgroundimg, (0,0))
    def ground(self):
        self.grx -= self.grspeed
        self.screen.blit(self.groundimg, (self.grx,500))
        width = 6720
        if self.grx == -width:
            self.screen.blit(self.groundimg, (width+self.grx,500))
            self.grx = 0
    def line(self):
        pygame.draw.line(self.screen, (255,255,255),(0,500), (1280, 500), self.Lwidth)
    # def gravity(self):
    #     if self.y <= (500-102):
    #         self.y += 3
    def iscoll(self,x1,x2,y1,y2):
        dis = math.sqrt(math.pow(x2-x1,2)+ math.pow(y2-y1,2))
        if dis>80:
            return False
        if dis<80:
            return True