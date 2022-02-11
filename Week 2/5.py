#Submit a solution for E-187639. XOR in an array.

l = list(map(int, input().split()))
if (len(l) == 1): 
    x = int(input())
    l.append(x)

n, x = l
arr = [0] * n
if n != 1: 
    for i in range(0, n): 
        arr[i] = x + (2 * i)
    
    for i in range(0, n): 
        if i != 0:
            arr[i] = arr[i] ^ arr[i - 1]    
    
    print(arr[n - 1])

else: 
    print (x)