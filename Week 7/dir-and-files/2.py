'''
Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
'''
import os

path = os.chdir(os.getcwd())
if os.access("Week 7", os.F_OK):
    print("path exists")
else: 
    print("path does not exist") 
if os.access("Week 8", os.R_OK): 
    print("path is readable")
else: 
    print("path is not readable") 
if os.access("Week 8", os.W_OK): 
    print("path is writable")
else: 
    print("path is not writable") 
if os.access("Week 8", os.X_OK): 
    print("path is executable")
else: 
    print("path is not executable") 