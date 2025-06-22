age = int(input("Enter age : "))

try:
    if age<18:
        raise ValueError("age should be grt 18")
    else:
        print("age is not valid...")
except ValueError as e:
    print(f"{e}")
    