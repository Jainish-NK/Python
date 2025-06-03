def outer():
    print("Outer function called...")
    def inner():
        print("inner function called...")
    inner() #calling part

outer()