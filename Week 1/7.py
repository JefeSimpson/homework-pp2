#Submit a solution for G-195718. To decimal.
import math
'''
x = input()
result = 0

for i in range(0, len(x)):
    result += pow(2, len(x) - 1 - i) * int(x[i])

print(result)
'''
def toDecimal(x, pos):
    if x == "1" or x == "0":
        return int(x)
    if pos == len(x):
        return 0

    return (int(x[pos]) * pow(2, len(x) - 1 - pos)) + toDecimal(x, pos + 1)

binary = input()
print(toDecimal(binary, 0))
