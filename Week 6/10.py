'''
Write a Python program to convert a given camel case string to snake case.
'''
import re

text = "ThisIsCamelCaseString"
result = re.findall("[A-Z][a-z]*", text)

for i in range(len(result)): 
    if i != len(result) - 1: 
        print(result[i], end = "_")
    else:
        print(result[i])