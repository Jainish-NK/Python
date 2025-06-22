data = ["naman","bob","raj","parth"]

with open("./File/palimdrom.txt","w") as file:
    for i in data:
        if i == i[::-1]:
            file.writelines(i + '\n')

