from files.canvas_obj import Obj

class Enemy(Obj):
    def __init__(self) -> None:
        super().__init__()
    def render(self,x,y):
        self.screen.blit(self.enemyimg, (x,y))
    def spawn(self):
        pass