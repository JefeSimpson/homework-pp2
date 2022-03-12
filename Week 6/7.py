'''
Write a python program to convert snake case string to camel case string.
'''
import re

txt = "this_game_has_bullied_me"
result = re.split("_", txt)
for i in result: 
    print(i.capitalize(), end = "")
