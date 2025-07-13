import numpy as np
from PIL import Image

class Square:
    def __init__(self,x,y,side,color):
        self.x=x
        self.y=y
        self.side=side
        self.color=color

    def draw(self,canvas):
        canvas.data[self.x:self.x+self.side,self.y:self.y+self.side]=self.color


class Rectangle:
    def __init__(self,x,y,width,height,color):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
    def draw(self,canvas):
        canvas.data[self.x:self.x+self.height,self.y:self.y+self.width]=self.color

class Canvas:
    def __init__(self,width,height,color):
        self.width = width
        self.height = height
        self.color = color

        self.data = np.zeros((self.height,self.width,3),dtype=np.uint8)
        self.data[:]=self.color

    def make(self,imagepath):
        img = Image.fromarray(self.data,'RGB')
        img.save(imagepath)


canv = Canvas(width=300,height=300,color=(255,255,255))
squ = Square(10,10,100,(255,0,0))
squ.draw(canv)
rec = Rectangle(x=200,y=200,width=50,height=100,color=(0,255,0))
rec.draw(canv)
canv.make('canvas.png')
