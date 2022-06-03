from jumper.canvas_obj import Obj

class Enemy(Obj):
    def __init__(self) -> None:
        super().__init__()
    def render(self,x,y):
        self.screen.blit(self.enemyimg, (x,y))
    def spawn(self,x,y):
        if x <0-100:
            return (x+self.WIDTH+100)