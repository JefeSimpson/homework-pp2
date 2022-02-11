#Submit a solution for K-195846. Final essay.

s = input()
uniqueWords = set()
new_s = ""
for i in range(len(s)): 
    if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
        new_s += s[i]
    else: 
        if new_s != "":
            uniqueWords.add(new_s)
        new_s = ""
    
    if (i + 1 == len(s)) and new_s != "": 
        uniqueWords.add(new_s)
        
l = list(uniqueWords)
l.sort()
print(len(l))
for i in range(len(l)):
    print(l[i])