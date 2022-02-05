#Submit a solution for H-187532. First and last occurrence.

s = input()
t = input()

if s.find(t) != -1:
    str = "{} {}"
    if s.find(t) == s.rfind(t):
        print(format(s.find(t)))
    elif s.find(t) != s.rfind(t):
        print(str.format(s.find(t), s.rfind(t)))  
