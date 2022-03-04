'''
Write a Python program to calculate the area of a trapezoid.
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5
'''
import math

def area(a, b, h): 
    return (((a + b) / 2) * h)

h = 5
a = 5
b = 6
print(area(a = a, b = b, h = h))