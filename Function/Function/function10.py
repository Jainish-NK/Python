def commerce():
    print("user has taken admission in commerce")

def arts():
    print("user has taken admission in arts")

def science():
    print("user has taken admission in science")




#cd call back...
def admission(cd):
    #cd == commerce

    print("admission function called...")
    cd() #commerce arts science

pers = float(input("Enter Your pers"))
if pers > 80:
    admission(science)
elif pers > 70:
    admission(commerce)
else:
    admission(arts)
    
