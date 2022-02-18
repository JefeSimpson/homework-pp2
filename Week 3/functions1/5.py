'''
Write a function that accepts string from user and print all permutations of that string.
'''

def permutations(s): 
    if len(s) == 1:
        return s
    perm_set = set()
    for c in s: 
        for p in permutations(s.replace(c, '', 1)):
            perm_set.add(c + p)
    
    return perm_set


s = input()
print(permutations(s))