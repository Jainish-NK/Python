with open("./File/python.txt","r") as file:
    print("pos of cur :",file.tell())
    print(file.read(5))
    print("pos of cur :",file.tell())
    file.seek(0)
    print("pos of cur :",file.tell())
    print(file.read(5))
