def goa(name):
    print("goa function called...")
    return "KAJU"

def dubai(name):
    print("dubai function called...")
    return "KHAJUR"

def kashmir(name):
    print("kashmir function called...")
    return "shindoor"


def trip(cd):
    print("trip function called...")
    return cd("ram")

data = None
budget = int(input("Enter budget"))
if budget > 60000:
    data = trip(kashmir)
elif budget > 50000:
    data = trip(goa)
elif budget > 10000:
    data = trip(goa)

print("data = ",data)

