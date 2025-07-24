class Account:
    def __init__(self,acc_holder,balance):
        self.acc_holder=acc_holder
        self.balance=balance

    def deposit(self,amount):
        return self.balance+amount
    def withdraw(self,amount):
        return print("Transaction Sucessful! Balance:",self.balance-amount) if amount<self.balance else print("Insufficient Balance")
    def get_balance(self):
        return self.balance
    
acc1=Account("Abdul",5000)
acc2=Account("Zain",400)
print(acc1.acc_holder)
print(acc1.deposit(500))
print(acc1.withdraw(3500))
print(acc2.acc_holder)
print(acc2.withdraw(1000))