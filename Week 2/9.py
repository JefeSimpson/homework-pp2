#Submit a solution for I-77244. Discs.

n = int(input())

queue = []
for i in range(n):
    inputs = list(map(str, input().split()))
    if (len(inputs) == 1 and inputs[0] == '2'): 
        if len(queue) != 0:
            print(queue.pop(0), end = ' ')
    else:
        oper, disk = inputs
        if oper == '1':
            queue.append(disk)
