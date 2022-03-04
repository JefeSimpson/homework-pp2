'''
Write a program using generator to print the even numbers 
between 0 and n in comma separated form where n is input 
from console.
'''

def generator(n): 
    for i in range(n): 
        if i % 2 == 0 and (n - 1) - i > 1:
            yield str(i) + ', '
        if i % 2 == 0 and (n - 1) - i <= 1:
            yield str(i)
global n
n = int(input())

for i in generator(n): 
    print(i, end = "")

