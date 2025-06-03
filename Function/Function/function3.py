#default argument

def add(a=10,b=20):
    return a+b
print(add(100,20))
print(add())



def greet(name="jainish"):
    print("hello," , name)

greet("vidhi")
greet()



def bill(customer,amount,discount=0):
    total = amount - discount
    print(f"customer: {customer} has to pay: {total}")

bill("jainish",500,50)
bill("vidhi",100)