'''
name = input("\nEnter The Name : ")
upperName = ""

for i in name:
    if ord(i)>=97 and ord(i)<=122:
        upperName = upperName + chr(ord(i)-32)
    else:
        upperName = upperName + i

print(upperName)
'''

name = input("\nEnter The Name : ")
lowerName = ""

for i in name:
    if ord(i)>=65 and ord(i)<=97:
        lowerName = lowerName + chr(ord(i)+32)
    else:
        lowerName = lowerName + i

print(lowerName) 