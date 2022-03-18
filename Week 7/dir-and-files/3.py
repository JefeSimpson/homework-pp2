'''
Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
'''
import os

path = "E:\\Project PP2\\Week 7\\dir-and-files\\1.py"

if os.path.exists(path): 
    if os.path.isfile(path): 
        print("File name:", os.path.basename(path))
        print("Directory name:", os.path.dirname(path))
    else: 
        print("It's not a file")
        print("Directory name:", os.path.dirname(path))
else:
    print("path does not exist")