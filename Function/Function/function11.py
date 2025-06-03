def commerce(name):
    print(f"{name} has taken admission in commerce")

def science(name):
    print(f"{name} has taken admission in science")


def arts(name):
    print(f"{name} has taken admission in arts")


#cb call back...
def admission(cb,name):
    print("admission function called...")
    #cb("ram") #commerce arts science
    cb(name)

name = input("Enter Name : ")
pers = float(input("Enter your pers : "))
if pers > 80:
    admission(science,name)
elif pers > 70:
    admission(commerce,name)
else:
    admission(arts,name)


