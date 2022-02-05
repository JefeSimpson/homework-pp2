#Submit a solution for D-186885. Asman + Systems = Astems

num = int(input())
z_command = input()

if z_command == 'k':
    c = int(input())    
    result = str(round(float(num / 1024), c))
    for x in range (c - 1):
        result += '0'
    print(result)
elif z_command == 'b':
    print(num * 1024)