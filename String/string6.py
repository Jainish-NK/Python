name = input("Enter The Name : ")
convetedName = ""

for i in name:
    if " " not in i:
        convetedName += i

print(convetedName)