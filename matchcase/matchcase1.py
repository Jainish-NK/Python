'''

switch(choice)
{
    case 1:
    break;
}
'''

no1 = int(input("\nEnter The No1 : "))
no2 = int(input("\nEnter The No2 : "))

print("\nEnter The Below Choice : ")
print("\n1..Addition")
print("\n2..Subtraction")
print("\n3..Multiplication")
print("\n4..Division")
print("\n5..Exit")

choice = int(input())

match choice:
    case 1: 
        ans = no1+no2
        print("Add = ",ans)

    case 2:
        ans = no1-no2
        print("Sub = ",ans)

    case 3:
        ans = no1*no2
        print("Multiplication : ",ans)

    case 4:
        ans = no1/no2
        print("Division : ",ans)

    case _: 
        print("Invalid choice..")
