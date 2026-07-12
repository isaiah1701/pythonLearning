class bankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self):
        self.balance = self.balance + 50 
        return self.balance
    
    def withdraw(self):
        self.balance = self.balance - 50 
        return self.balance 
    
    def show_balance(self):
        return f"Your current balance is {self.balance}"


account1 = bankAccount("Bob",100)
account2 = bankAccount("Lenny",200)


account1.withdraw()
account2.deposit()

print(account1.show_balance())
print(account2.show_balance())