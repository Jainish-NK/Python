#public     self.name     everywhere
#protected  self._name    limited
#private    self.__name   not diectly accessible..

class BankAccount():

    def __init__(self,owner,balance):
        self.owner = owner #public 
        self.__balance = balance #private..
        self._emi = 19000

    def deposit(self,amount):
        if amount>0:
            self.__balance += amount

    def get_Balance(self):
        return self.__balance
    
account = BankAccount("Ram",5000)
account.deposit(4000)
print(account.get_Balance())
#print(f"account balance = {account.__balance}")        
print(f"emi = {account._emi}")

