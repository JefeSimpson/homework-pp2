'''
Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
'''
import re

pattern = "^a.*b$"
txt = "aldfjgkldfjnghkjdfb"
result = re.search(pattern, txt)
print(result)