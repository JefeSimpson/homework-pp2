'''
Write a Python program with builtin function to multiply all the numbers in a list
'''
import math

num_list = list(map(int, input().split()))

print(math.prod(num_list))
