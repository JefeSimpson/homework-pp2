'''
Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
'''

class Shape:
    area = 0
    def __init__(self):
        pass
    def area(self): 
        print(self.area)
        
class Square(Shape): 
    def __init__(self, lenght = 0): 
        Shape.__init__(self)
        self.lenght = lenght
    
    def area(self): 
        print(self.lenght * self.lenght)

s1 = Square(5)
s1.area()

Square().area()