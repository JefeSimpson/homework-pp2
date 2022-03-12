'''
Write a Python program to insert spaces between words starting with capital letters.
'''
import re

txt = "ThisIsThePlaceIWouldLikeToLive"
result = re.findall("[A-Z][a-z]*", txt)
for i in result: 
    print(i, end = " ")