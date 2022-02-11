#Submit a solution for B-187378. Maximum product of two elements.

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

if (len(arr) >= 2): 
    print(arr[n - 1] * arr[n - 2])
