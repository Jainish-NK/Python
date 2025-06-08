class User:

        def __init__(self,username,email,password):
                
                self.username = username
                self.email = email
                self.password = password

        def display(self):
                print(f"username : {self.username} \nEmail : {self.email} \nPassword : {self.password}")


username = input("\nEnter The User Name  : ")
email = input("\nEnter The Email : ")
password = input("\nEnter The Password : ")


info = User(username,email,password)
info.display()