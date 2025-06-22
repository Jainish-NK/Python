name = "ram"
try:
    print(name[4])
except IndexError as e:
    print(f"{e}")