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

getData("royal","x")
