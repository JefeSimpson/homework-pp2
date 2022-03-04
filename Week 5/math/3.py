'''
Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
'''
import math

def area(n, l): 
    return (n * (l ** 2)) / (4 * math.tan(math.pi / n))

n = 4 
l = 25
print(round(area(n, l)))