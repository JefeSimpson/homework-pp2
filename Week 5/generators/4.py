'''
Implement a generator called squares to yield the square of all numbers from (a) to (b). 
Test it with a "for" loop and print each of the yielded values.
'''

def generator(a, b): 
    num = a
    while num <= b: 
        yield num**2
        num += 1
global a, b
a, b = list(map(int, input().split()))
x = generator(a, b)
for i in x: 
    print(i)