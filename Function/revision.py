def demo():
    print("Demo function called..")
demo()

def test(a:int,b:int):
    print(a)
    print(b)

test("jainish",90)
test("ram","khunt")
test(10,20)

def add(a,b)->str:
    print("add function called..")
    return a+b

ans = add(10,20)
print(ans)
print("ans = ",add(100,200))
print("ans = ",add("ram","shyam"))


def add(a=10,b=20):
    return a+b
print(add(10,30))
ans = add()
print(ans)
print(add())

def greet(name="jainish"):
    print("hello ",name)

greet()
greet("vidhi")


def bill(custmor,amount,discount=0):
    total = amount - discount
    print(f"custmor : {custmor} has to pay bill {total}")

bill("jainish",500,30)
bill("vidhi",200)

def getUsers(user):
    print(user)

getUsers("jainish")
getUsers(["jainish","vidhi","kunj"])

def getStudents(*args):
    print(args)

getStudents()
getStudents("jainish","kunj","vidhi")

def test(x,y,*args):
    print(args)
    print(x)
    print(y)
test(10,20,30,40,50)

def getUserDetails(name,age,email,status):
    print(f"Name : {name} , Age : {age} , Email : {email} , status : {status}")

getUserDetails(name="vidhi",age="17",email="khuntvidhi78@gmail.com",status="false")


def getStudentData(*args,x):
    print("args : ",args)
    print("x ",x)

getStudentData("ram","shyam","amit","jai",x="JAINISH")


# def getStudentdetails(**kwargs):
#     print(kwargs)

def getStudentDetails(x,**kwargs):
    print(kwargs)
    print(x)

getStudentDetails(name="kunj",age=12,status="true",city="surat",x=10)


def demo(*args,**kwargs):
    print(args)
    print(kwargs)

demo(10,True,"ok",name="jainish",price=10000)

a = 100
t1 = type(a).__name__
print(t1)


def greet(name):
    return f"Hello {name}"

x = greet
ans = x("khunt")
print(ans)
print(x("jainish"))

def tobecalled():
    print("to be called...")

def test(a):
    print("Tset function called...")
    a() #tobecalled

test(tobecalled)

'''
def science():
    print("user has tacken admiission in sci")

def arts():
    print("user has tacken admiision in arts")

def commerce():
    print("user has tacken addmission in commerce")

def admission(cb):

    print("admission function called...")
    cb()

pers = float(input("\nEnter your pers : "))
if pers > 80:
    admission(science)
elif pers > 70:
    admission(commerce)
else:
    admission(arts)
'''

'''
def science(name):
    print(f"{name} has tacken admiission in sci")

def arts(name):
    print(f"{name} has tacken admiision in arts")

def commerce(name):
    print(f"{name} has tacken addmission in commerce")

def admission(cb,name):

    print("admission function called...")
    cb(name)

name = input("Enter Name : ")
pers = float(input("\nEnter your pers : "))
if pers > 80:
    admission(science,name)
elif pers > 70:
    admission(commerce,name)
else:
    admission(arts,name)
'''

# def goa(name):
#     print("goa function called....")
#     return "KAJU"

# def kashmir(name):
#     print("kashmir function called...")
#     return "shindoor"

# def dubai(name):
#     print("dubai function called...")
#     return "KHAJUR"

# def trip(cb):
#     print("trip function called...")
#     x = cb("ram")
#     print("x",x)

# budget = int(input("\nEnter Budget : "))
# if budget > 60000:
#     trip(kashmir)
# elif budget > 50000:
#     trip(goa)
# elif budget > 10000:
#     trip(dubai)

'''
def dubai(name):
    print("dubai function called...")
    return "KHAJUR"

def goa(name):
    print("goa function called...")
    return "KAJU"

def kashmir(name):
    print("kashmir function called...")
    return "Shindoor"

def trip(cb):
    print("trip function called....")
    x = cb("ram")
    return x

data = None
budget = int(input("\nEnter The Budget : "))
if budget > 60000:
    data = trip(kashmir)
elif budget > 50000:
    data = trip(goa)
elif budget > 10000:
    data = trip(dubai)

print("data = ",data)
'''
'''
def dubai(name):
    print("dubai function called...")
    return "KHAJUR"

def goa(name):
    print("goa function called...")
    return "KAJU"

def kashmir(name):
    print("kashmir function called...")
    return "Shindoor"

def trip(cb):
    print("trip function called....")
    return cb("ram")

data = None
budget = int(input("\nEnter The Budget : "))
if budget > 60000:
    data = trip(kashmir)
elif budget > 50000:
    data = trip(goa)
elif budget > 10000:
    data = trip(dubai)

print("data = ",data)
'''

def findMax(*args):
    return max(args)

ans = findMax(20,390,489,26,78)
print(ans)

def check_th(th,*args):
    return [i for i in args if i>th]

print(check_th(400,90,389,738,893,728,893,903))


def group_by_type(*args):
    return {t:[i for i in args if type(i).__name__ == t] for t in set(type(arg).__name__ for arg in args)}

print(group_by_type(10,20,30,90.90,"java",False,True,"jainish"))


#lamda 

test = lambda x :print(x)
test(100)

test = lambda x,y : print(x+y)
test(10,20)

test = lambda a,b,c : a+b+c
print(test(10,20,30))


even_or_odd = lambda x : "even" if x%2==0 else "odd"
print(even_or_odd(101))

maaimum = lambda a,b : a if a>b else b
print(maaimum(-903,-1000))

pass_or_fail = lambda marks : "pass" if marks > 34 else "Fail"
print(pass_or_fail(34.5))

check_num = lambda x : "poss" if x > 0 else "negative"
print(check_num(-0))

grade = lambda pers : "A" if pers > 80 else ("B" if pers > 70 else "C")
print(grade(90))


users = ["ram","shyam","bob","madam","naman"]


def checkPalimdrom(x):
    flag = True
    for i in x:
        if i != i[::-1]:
            flag = False
        return flag

test = lambda x : checkPalimdrom(x)
print(test(users))

#inner 

def outer():
    print("Outer function called...")
    def inner():
        print("inner function called...")
    inner()
outer()


def login_system(username,password):

    def validate_user():

        return username == "ADMIN" and password == "ADMIN"

    valid = validate_user()

    if(valid):
        print("user is valid...")
    else:
        print("user is not valid...")

login_system("ADMIN","Admin")



#generator

def my_fun():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

gen = my_fun()

for i in gen:
    print(i)

# print(next(gen))
print("----------------------------------------")

num = [1,2,3,4,5,6,7,8,9,10,203,304,103,19,13,11,32,35,135,19]

def even_num(data):
    for i in data:
        if i%2 ==0:
            yield i

x = even_num(num)

for i in x : 
    print(i)


def get_user(batch_size=10):
    total = 100
    for i in range(0,total,batch_size):

        batch = []
        for j in range(i,min(i+batch_size,total)):
            batch.append(j)
        yield batch

for b in get_user():
    print(b)


#decorators

def order_food(func):

    def inner():
        print("order foos")
        func()
    return inner

@order_food
def throw_party():
    print("throw partty function called...")

throw_party()


def procees_payment(func):

    def inner():
        print("proceesing Payment...")

        payment_successfully = True

        if payment_successfully:
            print("order conformed!")
            func()
        else:
            print("payment failed...")
    return inner

@procees_payment
def place_order():
    print("placing your order...")
place_order()


def loginRequired(func):

    def inner():
        name = input("Enter The Name : ")
        Role = input("Enter The Role : ")

        if name == "JAINISH" and Role == "JAINISH":
            func()
        else:
            print("user is not valid....")

    return inner

def access_data():
    print("user is accessing data....")

access_data()


def order_food(func):

    def inner(noofpersons):
        print(noofpersons)
        func(130)
    return inner

@order_food
def throw_party(persons):
    print("throwing party...",persons)

throw_party(100)


def isValid(func):

    def inner(data,query):
        flag = False
        if query in data:
            flag = True

        if flag:
            func()
        else:
            print("String is not valid...")
    return inner

@isValid
def getData():
    print("data is valid...")

getData("Royal","R")


def isValid(func):

    def inner(data,query):
        flag = False
        if query in data:
            flag = True

        if flag:
            func(data)
        else:
            print("String is not valid...")
    return inner

@isValid
def getData(data):
    print("data is valid...",data)

getData("Royal","x")


def int_only(func):
    def inner(*args):
        flag = True
        for i in args:
            if not isinstance(i,int):
                flag = False
                break
        if flag:
            print("valid")
            func(*args)
        else:
            print("Invalid")
    return inner

def getData(*args):
    print("data is valid...",*args)

getData(1,2,90,90,398)

numbers = [1,2,3,4,5]
#sq_numbers = [i**2 for i in numbers]
#sq_numbers = list(map(lambda x : x**2 , numbers))
#sq_numbers = tuple(map(lambda x : x**2 , numbers))
sq_numbers = set(map(lambda x : x**2,numbers))
print(sq_numbers)

name = "ahmedabad"
upper_case = map(lambda x : x.upper(),name)
print(list(upper_case))


data = ["amit","sumit","jay","raj","parth","kunal","smit","sanjay"]
upper_case = list(map(lambda x : x.upper(),data))
print(upper_case)

'''
sales = [100,200,300,400,500,600,700]
dis = float(input("\nEnter The discount : "))

sales_list = list(map(lambda x : x*(1-dis/100) , sales))
print(sales_list)
'''

#filter

num = [1,2,3,4,5,6,7,8,9]
x = filter(lambda x : x%2==0,num)
print(list(x))



data = ["amit","sumit","jay","",None,"raj","parth",None,"kunal","smit","sanjay"]
x1 = filter(lambda x :x and len(x) > 4 , data)
print(list(x1))
x2 = filter(lambda x : x and x.startswith('s'),data)
print(list(x2))
x3 = filter(lambda x : x,data)
print(list(x3))


#filtermap

num = [1,2,3,4,5,6,7,8,9,10]
num = range(1,11)


ans = filter(lambda x : x>30,map(lambda x : x**2 ,num))
print(list(ans))

data = ["amit","sumit","jai","raj","parth"]
ans1 = filter(lambda x : x.startswith('S'),map(lambda x : x.upper(),data))
print(list(ans1))

from functools import reduce

data = [i for i in range(11)]
ans = reduce(lambda x,y : x+y , data)
print(ans)

num = [10,203,40,50,202]
maxno = reduce(lambda x,y : x if x>y else y,num)
print(maxno)