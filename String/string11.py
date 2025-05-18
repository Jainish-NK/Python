data = "ahemedabad"

x = data[::]
x = data[1:3]
x = data[1:6:2]
x = data[::-1]
x = data[4::-1]
x = data[1:1]
print(x)

name = input("Enter Name")

if name == name[::-1]:
    print("name is palimdrom..")
else:
    print("name is not palimdrom..")