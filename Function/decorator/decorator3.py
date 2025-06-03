def loginRequired(func):

    def inner():
        name = input("Enter The Name : ")
        Role = input("\nEnter The Role : ")

        if name == "JAINISH" and Role  == "JAINISH":
            func()
        else:
            print("User is not valid...")

    return inner


def access_data():
    print("user is accessing data...")


access_data()