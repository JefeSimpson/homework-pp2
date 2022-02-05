#Submit a solution for J-Levy the cryptographer

x = input()
str = ""
n = 0
for i in range(len(x)):
    if (x[i] != " "):
        str += x[i]
        n += 1

    else:
        if n >= 3:
            print(str, end =" ")
        str = ""
        n = 0
    
    if(i + 1 == len(x)):
        if n >= 3:
            print(str, end =" ")