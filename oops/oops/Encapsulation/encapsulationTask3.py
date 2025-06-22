username = input("\nEnter The username : ")
email = input("\nEnter The email : ")
password = input("\nEnter The password : ")

class User:

    def __init__(self,**kwargs):
       self.info = kwargs

    def display(self):
        for key,value in self.info.items():
            print(f"{key} : {value}")

    
obj = User(username = username,email = email,password = password)
obj.display()
