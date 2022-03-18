'''
Write a Python program to write a list to a file.
'''

l = list(input().split())

my_file = open("E:\\Project PP2\\Week 7\\dir-and-files\\write_exercise.txt", "w")
for i in l: 
    my_file.write(i)
    my_file.write("\n")
my_file.close()