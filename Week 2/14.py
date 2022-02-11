#Submit a solution for N-194739. We got stronger.

import math

frags = []

while True: 
    kill = int(input())
    if kill == 0: 
        break
    else: 
        frags.append(kill)
players = []

for i in range(math.ceil(len(frags)/2)): 
    if i == math.ceil(len(frags)/ 2) - 1 and len(frags) % 2 == 1:
        players.append(frags[i])
        break 
    players.append(frags[i] + frags[len(frags) - i - 1])


for i in players:
    print(i, end = " ")

