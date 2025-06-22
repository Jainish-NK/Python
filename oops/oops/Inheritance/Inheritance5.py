class India:

    def __init__(self):
        self.country = "India"
        print("India class const called..")

    def indian(self):
        print("indian method called..")

class Gujarat(India):

    def __init__(self):
       super().__init__()
       self.state = "Gujarat"
       print("Gujarat class const called..")

    def Gujarati(self):
        print("Gujarati method called...")    
        print(f"Country name = {self.country}")


class Ahmedabad(Gujarat):
    
    def __init__(self):
        super().__init__() #invoking gujarat class const...
        self.city = "Ahmedabad"
        print("Ahmedabad class const called,,,")
    
    def Ahmedabadi(self):
        print("ahmedabdi method called...")        
        print(f"country name = {self.country} state name  = {self.state}")


a = Ahmedabad()        
a.Gujarati()
a.Ahmedabadi()
     