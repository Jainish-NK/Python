def int_only(func):
    def inner(*args):
        flag = True
        for i in args:
            if not isinstance(i, int):
                flag = False
                break
        if flag:
            print("Valid")
            func(*args)
        else:
            print("Invalid")
    return inner

@int_only
def getData(*args):
    print("Data is valid...", *args)

getData(1, 2, 3, 4)
