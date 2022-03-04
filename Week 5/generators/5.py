'''
Implement a generator that returns all numbers from (n) down to 0.
'''

class first_n:
    def __init__(self, n):
        self.num = n
        self.till = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num > self.till:
            cur =  self.num
            self.num = self.num - 1
            return cur
        else:
             raise StopIteration()

myClass = first_n(50)
myIter = iter(myClass)

for x in myIter:
    print(x)