#Submit a solution for B-196111. Boris the Chef.

x = str(input())
asciiSum = 0
for y in x:
    asciiSum += ord(y)

if asciiSum > 300:
    print("It is tasty!")
else: 
    print("Oh, no!")