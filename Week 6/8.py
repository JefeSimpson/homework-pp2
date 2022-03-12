'''
Write a Python program to split a string at uppercase letters.
'''
import re

txt = "HelloThisIsMyKingdom"
result = re.findall("[A-Z][a-z]*", txt)
print(result)