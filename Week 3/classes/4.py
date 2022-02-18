'''
Write the definition of a Point class. Objects from this class should have a

a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points
'''

import math

class Point: 
    def __init__(self, x, y): 
        self.x = x
        self.y = y
    def show(self): 
        return self.x, self.y   
    def move(self, x, y):
        self.x += x
        self.y += y
    def dist(self, x, y): 
        return math.sqrt(pow(x - self.x, 2) + pow(y - self.y, 2))

p = Point(2 ,3) 
point_tuple = p.show()
print(point_tuple)
p.move(4, 2)
print(p.dist(2, 3))