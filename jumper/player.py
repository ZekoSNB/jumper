from jumper.canvas_obj import CanvObj
import pygame
from enum import IntEnum

class PlayerState(IntEnum):
    NOJUMP = 0
    CROUCH = 1
    JUMP = 2

class Player(CanvObj):
    def __init__(self,x,y,screen,height) -> None:
        super().__init__(x,y,screen)
        playerc0 = pygame.image.load('assets/images/alien1.png')
        playerc1 = pygame.image.load('assets/images/alien1_crouch.png')
        self.pli = [playerc0, playerc1, playerc0]
        for i,item in enumerate(self.pli):
            self.pli[i]= pygame.transform.scale(item, (100,100))
        
        self.height = height
        #* Mass of player once it's negative this causes the player to fall down
        self.mass = 1
        #* Falling speed; Value that subtract from speed so player doesn't stop instantly, but starts stopping slowly
        self.fall = 0.2
        self.state = PlayerState.NOJUMP 

    def render(self):
        #* Checks the state of player if player's state is jump
        if self.state == PlayerState.JUMP:
            F = (1/2)*self.mass*(self.height**2) #* Jump/Kinetic energy formula 
            self.y -= F #* Moving the player Y 
            self.height -= self.fall  #* subtracting height/speed to make jump smooth
            #* Once the player reaches it's jump limit the mass turns down and player starts falling down
            if self.height<0:
                self.mass=-1
            if self.y >= 400:
                self.y = 400
                self.mass = 1
                self.height = 5.8
                self.state = PlayerState.NOJUMP
        self.screen.blit(self.pli[self.state], (self.x,self.y))
        
    def jump(self):
        #* set Player's state to jump so once render is called it'll jump
        self.state = PlayerState.JUMP
    
    def crouch(self):
        if self.state != PlayerState.JUMP:
            #* Player starts crouching/ imitating jump
            self.state = PlayerState.CROUCH