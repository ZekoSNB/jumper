from jumper.canvas_obj import Obj
import pygame
class Enemy(Obj):
    def __init__(self,x,y,screen,speed) -> None:
        super().__init__(x,y,screen)
        self.enemyimg = pygame.image.load('assets/images/enemy1.png')
        self.enemyimg = pygame.transform.scale(self.enemyimg, (80,80))
        self.speed = speed
    def render(self):
        self.screen.blit(self.enemyimg, (self.x,self.y))
    # def spawn(self,x,y):
    #     if x <0-100:
    #         return (x+self.WIDTH+100)