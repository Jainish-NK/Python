s = "PyTHon"
swapCase = ""

for i in s:
    if('A' <= i <= 'Z'):
        swapCase += chr(ord(i)+32)
    elif('a' <= i <='z'):
        swapCase += chr(ord(i)-32)
    else:
        swapCase += i
print(swapCase)