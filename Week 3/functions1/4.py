'''
You are given list of numbers separated by spaces. 
Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
'''

def filter_prime(directory):
    for i in directory:
        isPrime = True
        if i!= 0 and i != 1: 
            for j in range(2, int(i / 2) + 1): 
                if i % j == 0: 
                    isPrime = False
        else: 
            isPrime = False
        if isPrime: 
            print(i, end = " ")

            
l = list(map(int, input().split()))  
filter_prime(l)    