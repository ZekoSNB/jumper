from jumper.canvas_obj import CanvObj
import pygame
from enum import IntEnum

class PlayerState(IntEnum):
    NOJUMP = 0
    CROUCH = 1
    JUMP = 2

class Player(CanvObj):
    def __init__(self,x,y,screen,speed) -> None:
        super().__init__(x,y,screen)
        playerc0 = pygame.image.load('assets/images/alien1.png')
        playerc1 = pygame.image.load('assets/images/alien1_crouch.png')
        playerc2 = pygame.image.load('assets/images/alien1_crouch2.png')
        self.pli = [playerc0, playerc1, playerc0]
        for i,item in enumerate(self.pli):
            self.pli[i]= pygame.transform.scale(item, (100,100))
        self.speed = speed
        self.mass = 1
        self.fall = 0.2
        self.state = PlayerState.NOJUMP 

    def render(self):
        if self.state == PlayerState.JUMP:
            F = (1/2)*self.mass*(self.speed**2) #* Jump/Kinetic energy formula 
            self.y -= F # Moving the player Y 
            self.speed -= self.fall  # slowing speed down
            if self.speed<0:
                self.mass=-1
            if self.y >= 400:
                self.y = 400
                self.mass = 1
                self.speed = 5.8
                self.state = PlayerState.NOJUMP
        self.screen.blit(self.pli[self.state], (self.x,self.y))
        
    def jump(self):
        self.state = PlayerState.JUMP
    
    def crouch(self):
        if self.state != PlayerState.JUMP:
            self.state = PlayerState.CROUCH