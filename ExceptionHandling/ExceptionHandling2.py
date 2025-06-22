try:
    age = int(input("Enter age "))
    print(f"age = {age}")
except ValueError as e:
    print("error ",e)
finally:
    print("finally....")