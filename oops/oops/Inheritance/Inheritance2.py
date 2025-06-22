class Gov:

    rulingParty = "BJP" # class variable...
    
    def __init__(slef):
        print("Gov class const called...")

    def applyTax(self):
        self.tax = 10 #instance variable... Gov    

class StateGov(Gov):

    def __init__(self):
        print("StateGov class const called...")
    
    def  getTax(self):
        print(f"tax from gov = {self.tax}")


s = StateGov()
s.applyTax()
s.getTax()


