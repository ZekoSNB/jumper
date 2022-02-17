import pygame
from files.canvas_obj import object

class Game(object):
    def __init__(self) -> None:
        super().__init__()
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.quit = False

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit = True
    def run(self):
        while not self.quit:
            self.event()
            pygame.display.update()