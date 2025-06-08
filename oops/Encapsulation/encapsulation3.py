class Student:

    collageName = "PDEU" #calss level var...

    def getStudentName(self,name):
        #name = local variable...
        #self.name = instance variable.
        self.name = name

stu = Student()
stu.getStudentName("Jainish")
print(f"collage Name = {stu.collageName} student name = {stu.name}")