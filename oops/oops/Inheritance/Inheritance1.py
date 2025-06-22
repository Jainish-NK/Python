class Parent:

    def parentFunction(self):
        print("parent class function called..")

class Child(Parent):

    def childFunction(self):
        print("child class function called..")
        self.parentFunction()


c = Child()
c.childFunction()
c.parentFunction()