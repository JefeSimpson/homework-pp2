'''
Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
Withdrawals may not exceed the available balance. 
Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
'''

class Account: 
    owner = ""
    balance = 0
    def __init__(self, owner, balance): 
        self.owner = owner
        self.balance = balance
    def deposit(self, money): 
        self.balance += money
    def withdraw(self, money): 
        if self.balance < money:
            print("Insufficient funds")
        else: 
            self.balance -= money

p = Account("Rebecca", 320)
p.withdraw(300)
p.balance
p.withdraw(20)
p.balance
p.withdraw(10)
