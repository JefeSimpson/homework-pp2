#Submit a solution for O-147221. String calculator.

def conver(func): 
    if func == 'ONE': 
        return '1'
    if func == 'TWO': 
        return '2'
    if func == 'THR': 
        return '3'
    if func == 'FOU': 
        return '4'
    if func == 'FIV': 
        return '5'
    if func == 'SIX': 
        return '6'
    if func == 'SEV': 
        return '7'
    if func == 'EIG': 
        return '8'
    if func == 'NIN': 
        return '9'
    if func == 'ZER': 
        return '0'
    if func == '1': 
        return 'ONE'
    if func == '2': 
        return 'TWO'
    if func == '3': 
        return 'THR'
    if func == '4': 
        return 'FOU'
    if func == '5': 
        return 'FIV'
    if func == '6': 
        return 'SIX'
    if func == '7': 
        return 'SEV'
    if func == '8': 
        return 'EIG'
    if func == '9': 
        return 'NIN'
    if func == '0': 
        return 'ZER'
    

s = input() 
plus = False
str1 = ""
str2 = ""
helper = ""
count = 0
for i in range(len(s)):
    if count == 3 and plus == False:
        str1 += conver(helper)
        count = 0
        helper = ""
    if (count == 3 and plus == True):  
        str2 += conver(helper)
        count = 0
        helper = ""  
    if s[i] != '+': 
        helper += s[i]
        count += 1
    else: 
        plus = True
    if i + 1 == len(s) and plus == True: 
        str2 += conver(helper)
    
result = int(str1) + int(str2)
result = str(result)
for i in range(len(result)): 
    print(conver(result[i]), end = "")