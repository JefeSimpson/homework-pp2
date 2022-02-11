#Submit a solution for H-Closest point
import math

x, y = list(map(int, input().split()))

n = int(input())
pair_list = []
for i in range(n): 
    x1, y1 = list(map(int, input().split()))
    distance = math.sqrt(pow(x1 - x, 2) + pow(y1 - y, 2))
    pair_list.append([x1, y1, distance])

pair_list = sorted(pair_list, key = lambda num: num[2])

for i in range(len(pair_list)): 
    print(pair_list[i][0], end = " ")
    print(pair_list[i][1])
