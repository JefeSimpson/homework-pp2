'''
Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
'''

word = "WellYouMayCountThis"
up_count = 0
low_count = 0
for i in word:
    if i.islower(): 
        low_count += 1
    if i.isupper(): 
        up_count += 1

print("upper letters count", up_count)
print("lower letters count", low_count)
