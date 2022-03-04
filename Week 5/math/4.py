'''
Write a Python program to calculate the area of a parallelogram.
Length of base: 5
Height of parallelogram: 6
Expected Output: 30.0
'''
import math

def area(a, h):
    return float(a * h)

a = 5
h = 6
print(round(area(a, h), 1))