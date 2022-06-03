from jumper.canvas_obj import CanvObj
import pygame


class Player(CanvObj):
    def __init__(self,x,y,screen,speed) -> None:
        super().__init__(x,y,screen)
        self.playerc = pygame.image.load('assets/images/alien1.png')
        self.playerc1 = pygame.image.load('assets/images/alien1_crouch.png')
        self.playerc2 = pygame.image.load('assets/images/alien1_crouch2.png')
        self.playerc = pygame.transform.scale(self.playerc, (100,100))
        self.playerc1 = pygame.transform.scale(self.playerc1, (100,100))
        self.playerc2 = pygame.transform.scale(self.playerc2, (100,100))
        self.pli = [self.playerc,self.playerc1,self.playerc2]
        self.speed = speed
    def render(self,ind):
        self.screen.blit(self.pli[ind], (self.x,self.y))
        


