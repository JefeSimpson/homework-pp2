#Submit a solution for L-194034. Open Closed.

l = []
s = input()

for i in range(len(s)): 
    if s[i] == "{" or s[i] == "(" or s[i] == "[": 
        l.append(s[i])
    else: 
        if len(l) == 0:
            print("No")
            exit()
        elif ((s[i] == '}') and ('{' not in l)) or ((s[i] == ')') and ('(' not in l)) or ((s[i] == ']') and ('[' not in l )): 
            print("No")
            exit()
        else: 
            l.pop()
        

if len(l) == 0:
    print("Yes")
else:
    print("No")

        