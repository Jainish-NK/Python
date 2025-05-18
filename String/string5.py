name = input("Enter Name : ")
chr = input("Enter Chr : ")
flag = -1

for i in range(len(name)):
    if name[i] == chr:
        flag = i
        break

print(chr,"found at index",flag)