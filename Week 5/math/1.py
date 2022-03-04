'''
Write a Python program to convert degree to radian.
Input degree: 15
Output radian: 0.261904
'''
import math

def toRadian(deg):
    return math.radians(deg)

deg = 15
print(round(toRadian(deg), 6))

