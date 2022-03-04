'''
Create a generator that generates the squares of numbers up to some number N.
'''


def generator(n): 
    num = 0
    for i in range(n): 
        yield i**2

global n
n = int(input())
x = generator(n)
for i in x: 
    print(i)