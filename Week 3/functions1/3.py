'''
Write a program to solve a classic puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have? 
Create function: solve(numheads, numlegs):
'''

def solve(numheads, numlegs): 
    rabbits = int((numlegs / 2) - numheads)
    chickens = int(numheads - rabbits)
    print("rabbits: " + str(rabbits) + ", " + "chickens: " + str(chickens))


heads = int(input("heads: "))
legs = int(input("legs: "))
solve(numheads = heads, numlegs = legs)