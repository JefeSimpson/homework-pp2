'''
Write a Python program to copy the contents of a file to another file
'''
import os

path = "E:\\Project PP2\\Week 7\\dir-and-files"
os.chdir(path)
if not os.path.exists("main_file.txt"): 
    file_one = open("main_file.txt", "w")
    file_one.write("so \nhere i \nneed \nwrite")
    file_one.close()
file_one = open("main_file.txt", "r")
file_two = open("copy_file.txt", "w")

for line in file_one: 
    file_two.write(line)