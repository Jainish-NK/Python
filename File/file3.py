with open("./File/userdata.txt","a") as f:
    while True:
        name = input("enter name (or type exit for exit) : ")
        if name == "exit":
            break

        no1 = int(input("enter no1 : "))
        no2 = int(input("enter no2 : "))
        total = no1 + no2
        f.write(f"{name}:{total}")