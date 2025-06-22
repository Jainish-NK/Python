class Student:

    def __init__(self,name,rollno,age):
        print("Student class const called..")
        self.name = name
        self.rollno = rollno
        self.age = age
        
    
class  Display(Student):
    
    def display(self):
        print("Name : ",self.name) 
        print("Roll No : ",self.rollno)
        print("Age : ",self.age)

s = Display("om",101,18)
s.display()    