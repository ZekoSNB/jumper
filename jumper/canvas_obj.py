import pygame,abc,math

class CanvObj(abc.ABC):
    def __init__(self,x,y,screen) -> None:
        self.x = x
        self.y = y
        self.screen = screen

    def is_colistion(self, other: 'CanvObj'):
        # x2 -=5
        # Collsion formula
        dis = math.sqrt(math.pow(self.enemy.x-self.player.x,2)+ math.pow(self.enemy.y-self.player.y,2))
        if dis>76:
            return False
        if dis<76:
            return True