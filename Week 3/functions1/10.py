'''
Write a Python function that takes a list and returns a new list with unique elements of the first list. 
Note: don't use collection set.
'''

def toUnique(l):
    u = []
    for i in l: 
        if i not in u: 
            u.append(i)
    for i in u: 
        print(i, end = " ")

l = list(map(str, input().split())) 
toUnique(l)
    


