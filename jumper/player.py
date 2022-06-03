from jumper.canvas_obj import Obj
import pygame


class Player(Obj):
    def __init__(self,x,y,screen,pli,speed) -> None:
        super().__init__(x,y,screen)
        self.pli = pli
        self.playerc = pygame.image.load('assets/images/alien1.png')
        self.playerc1 = pygame.image.load('assets/images/alien1_crouch.png')
        self.playerc2 = pygame.image.load('assets/images/alien1_crouch2.png')
        self.speed = speed
    def render(self,ind):
        self.screen.blit(self.pli[ind], (self.x,self.y))
        


