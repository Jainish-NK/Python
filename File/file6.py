with open("./File/mydata.txt","r") as file:
    header_p = False # false...
    while True:
        position = file.tell()
        print(position)
        line = file.readline()

        if not line:
            break

        if line.startswith("Header"):
            if not header_p:
                print("keeping Header",line.strip())
                header_p = True
            else:
                print("skipping header")
                #file.seek(file.tell())
        else:
            print(line.strip())
