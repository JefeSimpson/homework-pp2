'''
Write a Python program that invoke square root function after specific milliseconds.

Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858

'''
import math
import time

num = 25100
ms = 2123
time.sleep(ms / 1000)
print("Square root of", num, "after", ms, "miliseconds is", math.sqrt(num))
