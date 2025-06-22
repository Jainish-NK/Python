class User:

    def __init__(self,username,email,password):

        self.username = username
        self.email = email
        self.password = password

    def display(self):

      dis = {
         'username' : self.username,
         'email' : self.email,
         'password' : self.password
      }
      print(dis)

      
username = input("\nEnter The username : ")
email = input("\nEnter The email")
password = input("\nEnter The password")

info = User(username,email,password)
info.display()
