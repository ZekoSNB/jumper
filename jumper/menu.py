 #! UNUSED FILE 
import pygame


class Menu():

    def __init__(self) -> None:
        self.pause = pygame.Surface((1280,720))
        self.pause = self.pause.convert_alpha()

    def start(self):
        while True:
            self.screen.fill((0,0,0))
            self.textf('HI there')
            pygame.display.update()

    def gameover(self):
        pass
