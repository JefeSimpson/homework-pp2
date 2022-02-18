'''
Define a class named Rectangle which inherits from Shape class from task 2. 
Class instance can be constructed by a length and width. 
The Rectangle class has a method which can compute the area.
'''

class Shape:
    area = 0
    def __init__(self):
        pass
    def area(self): 
        print(self.area)

class Rectangle(Shape):
    def __init__(self, lenght, width): 
        Shape.__init__(self)
        self.lenght = lenght
        self.width = width
    
    def area(self): 
        print(self.lenght * self.width)

r = Rectangle(3, 5)
r.area()

