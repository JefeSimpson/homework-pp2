#Submit a solution for J-195834. Boris and Passwords.

n = int(input())
passwords = set()
for i in range(n):
    upperValid = False
    lowerValid = False
    numberValid = False 
    s = input()
    for j in range(len(s)): 
        if (s[j] >= 'A' and s[j] <= 'Z'):
            upperValid = True
        if (s[j] >= 'a' and s[j] <= 'z'):
            lowerValid = True
        if (s[j] >= '0' and s[j] <= '9'):
            numberValid = True

        
    if upperValid and lowerValid and numberValid:
        passwords.add(s)
        
l = list(passwords)
l.sort()
print(len(l))
for i in range(len(l)): 
    print(l[i])