'''
Write a program which can filter prime numbers in a list by using filter function. 
Note: Use lambda to define anonymous functions.
'''

def isPrime(number): 
    checker = True
    if number == 0 or number == 1: 
        checker = False
    for i in range(2, int(number / 2) + 1): 
        if number % i == 0: 
            checker = False
    if checker == True: 
        return number

def myFilter(numbers):
    print(list(filter(lambda x: isPrime(x), numbers)))

l = [1, 3, 4, 5, 6, 9, 10, 11, 12, 13, 16, 17]
myFilter(l)