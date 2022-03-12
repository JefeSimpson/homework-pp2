'''
Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
'''
import re

txt = "aaabb"
result = re.search("ab{2,3}", txt)
if result: 
    print("Match")
else:
    print("Not matched")