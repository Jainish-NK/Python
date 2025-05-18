name = input("\nEnter The Name")
revName = ""

for i in range(len(name)-1,-1,-1):
    revName = revName + name[i]

if name == revName:
    print("Palimdrom")
else:
    print("not palimdrom")
    