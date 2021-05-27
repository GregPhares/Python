import Shape
from Shape import *
class Triangle(Shape):
    def __init__(self,size):
        Shape.__init__(self)
        self.size= size
        
    def draw(self):
        super().draw()
        print("Triangle Draw")
        incre=1        
        for row in range(self.size):
            print("*"*incre)
            incre+=1
            