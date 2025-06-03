def goa(name):
    print("goa function called...")
    return "KAJU"

def dubai(name):
    print("dubai function called...")
    return "KHAJUR"

def kashmir(name):
    print("kashmir function called...")
    return "shindor"


def trip(cb):
    print("trip function called...")
    x = cb("ram")
    return x #kaju | shindoor | khajur

data = None
budget = int(input("Enter The Budget : "))
if budget > 60000:
    data = trip(kashmir)
elif budget > 50000:
    data = trip(goa)
elif budget > 10000:
    data = trip(dubai)

print("data = ",data)