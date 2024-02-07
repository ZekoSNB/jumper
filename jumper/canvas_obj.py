import abc,math

class CanvObj(abc.ABC):
    def __init__(self,x,y,screen) -> None:
        self.x = x
        self.y = y
        self.screen = screen

    def is_collision(self, other: 'CanvObj', zone) -> bool:
        #* Collision Formula
        dis = math.sqrt(math.pow(other.x-self.x,2)+ math.pow(other.y-self.y,2))
        return dis < zone

    @abc.abstractmethod
    def render(self):
        pass