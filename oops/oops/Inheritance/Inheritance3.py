class Member:

    def Info(self):
        self.name = input("Enter The name : ")
        self.age = int(input("Enter The age : "))

class LibraryMember(Member):

    def checkAge(self):
         if self.age>18:
            print(f"{self.name} can borrow books.")
         else:
             print(f"{self.name} cannot borrow books (underage).")

obj = LibraryMember()
obj.Info()
obj.checkAge()