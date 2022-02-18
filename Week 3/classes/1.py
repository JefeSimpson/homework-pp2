'''
Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
'''

class MyClass: 
    def getString(self, str_1):
        self.str_1 = str_1

    def printString(self): 
        print(self.str_1.upper())

str_1 = input()
c = MyClass()
c.getString(str_1)
c.printString()

