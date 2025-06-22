name = "ami t"

try:
    if " " in name:
        raise ValueError("space must not be there in str..")
    else:
        print(f"{name}")
except ValueError as e:
    print(f"{e}")