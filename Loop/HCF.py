a = int(input("\nEnter No1 : "))
b = int(input("\nEnter No2 : "))

#6 4
while b!=0:
    #temp = 4
    #temp = 2
    temp = b #4 , 2
    #b = 6 % 4 = 2
    #b = 4 % 2 = 0
    b = a%b

    a = temp 
    #a = 4
    #a = 2
print("a",a)