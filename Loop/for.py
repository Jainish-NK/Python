#1 to 10 using rang()

#for i in range(1,10):
 #   print(i)

#for i in range(1,11):
 #   print(i,end = " ")

#0 to n-1
#for i in range(10):
#    print(i,end = " ")

#for i in range(1,25,3):
#    print(i)

#for i in range(10,0,-1):
 #   print(i, end=" ")

sum = 0

no1 = int(input("\nEnter The no1 : "))
no2 = int(input("\nEnter The no2 : "))

for i in range(no1,no2):
    print(i,end=" ")
    sum = sum + i
    
print("\nThe Sum of Total No : ",sum)