#Submit a solution for C-187698. Diagonal x.

n = int(input())

for i in range(0, n): 
    for j in range(0, n): 
        if i == 0 and i != j: 
            print(j, end = " ")
        elif j == 0 and j != i:
            print(i, end = " ")
        elif i == j: 
            print(i * j, end = " ")
        else:
            print(0, end = " ")

    print()       