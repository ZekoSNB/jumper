from jumper.canvas_obj import CanvObj
import pygame
class Enemy(CanvObj):
    def __init__(self,x,y,screen,speed) -> None:
        super().__init__(x,y,screen)
        self.enemyimg = pygame.image.load('assets/images/enemy1.png')
        self.enemyimg = pygame.transform.scale(self.enemyimg, (80,80))
        self.speed = speed

    def render(self):
        #* moving the enemy
        self.x -= self.speed
        #* If enemy is behind player/border move it infront of player
        if self.x <= -90:
            self.x = 1360
        self.screen.blit(self.enemyimg, (self.x,self.y))