class Bank:

    def __init__(self,name,IFSC):
        print("bank const called...")
        self.name = name
        self.IFSC = IFSC

    def details(self):
        print(f"name of bank = {self.name}")
        print(f"IFSC of {self.name} = {self.IFSC}")

SBI = Bank("SBI","SBIN007")
SBI.details()

HDFC = Bank("HDFC","HDFC008")
HDFC.details()