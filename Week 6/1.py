'''
Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
'''
import re

txt = "abbbabb" 
pattern = "a{1}.b*"
result = re.search("a.b*", txt) 
result1 = re.search(pattern, txt)
if result: 
    print("Match")
else:
    print("Not matched")

print(result1)