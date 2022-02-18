'''
Read in a Fahrenheit temperature. 
Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion: C = (5 / 9) * (F – 32)
'''

def toCentigrade(temp): 
    c = (5 / 9) * (temp - 32)
    return c

temp = float(input())
print(toCentigrade(temp))