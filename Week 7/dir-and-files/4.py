'''
Write a Python program to count the number of lines in a text file.
'''
import os

f = open("E:\\Project PP2\\Week 7\\dir-and-files\\line_exercise.txt", "r")
lines_num = 0
for i in f: 
    lines_num += 1

print(lines_num)
