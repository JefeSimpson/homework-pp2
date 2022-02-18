'''
Write a function that computes the volume of a sphere given its radius.
'''

import math

def volumeCalc(r): 
    v = (4 / 3) * math.pi * pow(r, 3)
    return v

r = float(input())
print(volumeCalc(r))
