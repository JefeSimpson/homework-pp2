'''
Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
'''
import os

path = "E:\\Project PP2\\Week 7\\dir-and-files\\letters-file-dir"
os.chdir(path)
if not os.path.exists(path): 
    os.makedirs("letters-file-dir")
for letter in range(65, 91): 
    let = chr(letter)
    my_file = open(let + ".txt", "w")

    