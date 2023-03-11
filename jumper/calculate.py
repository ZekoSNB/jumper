import pygame

class Calculate():
    def __init__(self) -> None:
        pass

    def hover(self,x,y,height,width):
        self.mx, self.my = pygame.mouse.get_pos()
        is_inside = self.mx <= (x+width) and self.mx >= x and self.my<=(y+height) and self.my>= y

        if is_inside:
            return True
        else:
            return False