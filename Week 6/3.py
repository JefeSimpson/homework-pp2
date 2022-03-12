'''
Write a Python program to find sequences of lowercase letters joined with a underscore.
'''
import re

txt = "aaasdadfvbch_basdlzx"
txt1 = "Aslgsjksd_AALFkgfkg"
result = re.search("^[a-z]+_[a-z]+$",txt)
result1 = re.search("^[a-z]_+[a-z]$",txt1)
print(result)
print(result1)
