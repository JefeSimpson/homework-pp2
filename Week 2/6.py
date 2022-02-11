#Submit a solution for F-196670. Compensations.

n = int(input())

students = {}
max = 0
for i in range(n): 
    name, amount = input().split()
    amount = int(amount)
    if students.get(name) == None: 
        if amount > max: 
            max = amount
        students[name] = amount
    else: 
        taker = students[name]
        students[name] = taker + amount
        if (taker + amount) > max: 
            max = taker + amount
            
              
for i in sorted(students): 
    if students[i] == max:
        print (i + " is lucky!")
    else:
        difference = max - students[i]
        st1 = i + " has to receive {} tenge"
        print(st1.format(difference))