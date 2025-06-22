class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name : {self.name} , Age : {self.age}")

class Employee(Person):
    def __init__(self, name, age,emp_id,salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def show_employee(self):
        print(f"Emp Id : {self.emp_id} , Salary : {self.salary}")

class Manager(Employee):
    def __init__(self, name, age, emp_id, salary,dept_id):
        super().__init__(name, age, emp_id, salary)
        self.dept_id = dept_id

    def show_manager(self):
        self.show_info()
        self.show_employee()
        print(f"Department ID : {self.dept_id}")


obj = Manager("jainish",21,"E102",100000,"AI-ENGINEER")
obj.show_manager()
