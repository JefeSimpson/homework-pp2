'''
Write a Python program to list only directories, files and all directories, files in a specified path.
'''
import os

path = "E:\Project PP2\Week 7\dir-and-files"
# or path = os.getcwd()
print(os.getcwd())


l = os.listdir(path)
print(l)

dir_list = []
file_list = []
for i in l: 
    if os.path.isdir(os.path.join(path, i)):
        dir_list.append(i)
    else:
        file_list.append(i)

print("Directories list:", dir_list)
print("Files list:", file_list) 

