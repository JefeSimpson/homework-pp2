'''
Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
'''
import os

path = "E:\\Project PP2\\Week 7\\dir-and-files\\"
os.chdir(path)
path_file = "removable.txt"
path_dir = "removable-dir"
if os.path.exists(path_file): 
    os.remove(path_file)
else: 
    my_file = open(path_file, "w")
if os.path.exists(path_dir):
    os.rmdir(path_dir)
else: 
    os.makedirs(path_dir)
