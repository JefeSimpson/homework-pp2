#Submit a solution for D-188131. Tsunami.

n = int(input()) 

for i in range(1, n + 1): 
    if n % 2 == 0: 
        for lattices in range(0, i): 
            print("#", end = "")
        for dots in range(i, n):
            print(".", end = "") 
    else:
        for dots in range(i, n): 
            print(".", end = "")
        for dots in range(0, i):
            print("#", end = "") 
    
    print()