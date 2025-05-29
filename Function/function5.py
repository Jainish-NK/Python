#key word arguments

def getUserDetail(name,age,email,status):
    print(f"Name: {name}, Age: {age}, Email: {email}, Status: {status}")   

#getUserDetail("jainish","jainish89@gmail.com","19",True)
getUserDetail(name="vidhi",age="17",email="vidhi89@gmail.com",status=False)



def geStudentData(*args,x):
    print("args ",args)
    print("x ",x)

geStudentData("ram","shyam","amit","jay",x="jainish")
