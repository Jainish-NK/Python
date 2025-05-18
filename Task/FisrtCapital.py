name = input("\nEnter The Name : ")
name += " "
res=""
capital=True

for i in name:
    if capital and ('a' <= i <= 'z'):
        res += chr(ord(i)-32)
        capital = False
    else:
        res += i
        if i == " ":
            capital = True

print("RES : ",res)