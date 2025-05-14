'''
GRADE SYSTEM:
mark -->5 subject:
enter maths mark,...,...,..

per find:
pers> 80 : A grade
pers> 70 : B 
>60 : c
<60 : D
<35 fail

'''



mark1 = int(input("Enter The Mark1 : "))
mark2 = int(input("Enter The Mark2 : "))
mark3 = int(input("Enter The Mark3 : "))
mark4 = int(input("Enter The Mark4 : "))
mark5 = int(input("Enter The Mark5 : "))

total = mark1 + mark2 + mark3 + mark4 + mark5
per = total/5

print("Total Marks : ",total)
print("Persentage : ",per)

if per>=80:
    print("A Grade")
elif per>=70:
    print("B Grade")
elif per>=60:  
    print("C Grade")
elif per<60 and per>=35:
    print("D Grade")
elif per<35:
    print("FAIL")