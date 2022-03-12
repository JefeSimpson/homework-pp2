'''
Write a Python program to find the sequences of one upper case letter followed by lower case letters.
'''
import re

txt = "Awhatttawanna"
result = re.search("^[A-Z][a-z]+$", txt)
print(result)