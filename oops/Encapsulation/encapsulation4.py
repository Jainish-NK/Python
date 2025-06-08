class Bank:

    def __init__(self):
        print("Bank class const Called...")
        self.name = "SBI"
        self.IFSC = "SBIN007"

    def display(self):
        print(f"name of bank = {self.name}")
        print(f"IFSC OF {self.name} = {self.IFSC}")


SBI = Bank()
SBI.display()

HDFC = Bank()
HDFC.display()