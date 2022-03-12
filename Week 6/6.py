'''
Write a Python program to replace all occurrences of space, comma, or dot with a colon.
'''
import re

pattern = "[ .,]"
text = "Hello this is my home, and I wanna share it with you."
print(re.sub(pattern, ":", text))
