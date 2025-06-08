def isvalid(func):

    def inner(data,query):
        flag = False
        if query in data:
            flag = True


        if flag:
            func(data)  #getData(data)
        else:
            print("string is not valid...")
    
    return inner

@isvalid
def getData(data):
    print("data is valid...",data)

getData("Royal","R")
