from jumper.canvas_obj import Obj


class Player(Obj):
    def __init__(self) -> None:
        super().__init__()
    def render(self,ind,x,y):
        self.screen.blit(self.pli[ind], (x,y))
        
    def jump(self,y):
        self.y = y
        self.y -= self.speed
        return y
    def border(self,y):
        if y >= 400:
            return y
        


