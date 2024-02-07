import pygame

class Calculate():
    def __init__(self) -> None:
        pass

    def hover(self,x,y,height,width) -> bool:
        self.mx, self.my = pygame.mouse.get_pos()
        is_inside = self.mx <= (x+width) and self.mx >= x and self.my<=(y+height) and self.my>= y

        return is_inside