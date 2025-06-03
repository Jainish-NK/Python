#hof(highr order function)

def tobecalled():
    print("to be called....")

def test(a):
    #a=10
    #a = tobecalled

    print("test function called..")
    a() #tobecalled...

#test(10)
test(tobecalled)


