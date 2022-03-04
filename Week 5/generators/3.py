'''
Define a function with a generator which can iterate the numbers, 
which are divisible by 3 and 4, between a given range 0 and n.
'''

def generator(n): 
    for i in range(n): 
        if i % 3 == 0 and i % 4 == 0: 
            yield i
global n
n = int(input())
x = generator(n)
for i in x:
    print(i)