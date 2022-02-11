#Submit a solution for M-197032. Important dates.

year = []

while True: 
    l = list(map(str, input().split()))
    if l[0] == '0': 
        break
    d, m, y = l
    year.append([d, m, y])


year = sorted(year, key = lambda date: (date[2], date[1], date[0]))
for i in range(len(year)): 
    print(year[i][0], end = ' ')
    print(year[i][1], end = ' ')
    print(year[i][2])

