'''
Write a function that accepts string from user, return a sentence with the words reversed. 
We are ready -> ready are We
'''

def reverser(s): 
    str_result = ""
    str_parts = ""
    for i in range(len(s)): 
        if s[i] != " ": 
            str_parts += s[i]
        else: 
            str_result = str_parts + " " + str_result
            str_parts = ""
        if i == len(s) - 1: 
            str_result = str_parts + " " + str_result
            str_parts = ""
    
    return str_result

s = input()

print(reverser(s))
