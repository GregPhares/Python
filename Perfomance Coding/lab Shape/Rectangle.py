import Shape
from Shape import *
class Rectangle(Shape):
    def __init__(self,length,width):
        Shape.__init__(self)
        self.length = length
        self.width =width
    
    def draw(self):
        super().draw()
        print("Rectangle Draw")
        for length in range(self.length):
            print("*"*self.width)
    