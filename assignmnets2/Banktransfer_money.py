class BankAccount:
    def __init__(self, account_number):
        self.account_number=str(account_number)
        self.balance=0
    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            raise print("insufficient funds")
    def deposit(self, amount):
        self.balance+=amount
    def get_balance(self):
        return self.balance

def trasfer_amount(acc1, acc2, amount):
    acc1.withdraw(amount)
    acc2.deposit(amount)
        
pushavathi=BankAccount("001")
Nikhil=BankAccount("002")
pushavathi.deposit(13000)
Nikhil.deposit(15000)

print("Pushpa 1 balance:{}/-".format(pushavathi.get_balance()))
print("Nikhil 2 balance:{}/-".format(Nikhil.get_balance()))
print("transferring amount")
trasfer_amount(pushavathi,Nikhil,1200)
print("Pushpa 1 balance:{}/-".format(pushavathi.get_balance()))
print("Nikhil 2 balance:{}/-".format(Nikhil.get_balance()))

        
        
    