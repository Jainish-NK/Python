class InvalidAgeException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

name = input("Enter name ")

try:
    if " "in name:
        raise InvalidAgeException("space is there in str...")
    else:
        print(f"{name}")
except InvalidAgeException as e:
    print(f"{e}")