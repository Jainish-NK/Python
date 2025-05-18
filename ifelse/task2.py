'''
no1 = int(input("\nEnter The No1 : "))
no2 = int(input("\nEnter The No2 : "))
no3 = int(input("\nEnter The No3 : "))

if no1 == no2 and no2 == no3:
    print("\nAll Three number are equal:",no1)

elif no1 == no2:
    if no3 > no1:
        print("\nNo2 is greatest:",no3)
    elif no3 < no1:
        print("\nNo1 and No2 are equal and greater than No3 : ",no1)
    else:
        print("\nNo1 , No2 and No3 are equal..")

elif no2 == no3:
    if no1 > no2:
        print("\nNo1 is greatest:",no1)
    elif no1 < no2:
        print("\nNo2 and No3 are equal and greater than No1 : ",no2)
    else:
        print("\nNo1 , No2 and No3 are equal..")

elif no1 == no3:
    if no2 > no1:
        print("\nNo2 is greatest:",no2)
    elif no2 < no1:
        print("\nNo1 and No3 are equal and greater than No2 : ",no1)
    else:
        print("\nNo1 , No2 and No3 are equal..")

else:
    if no2 > no3:
        print("\nNo2 is the Greatest:",no2)
    else:
        print("\nNo3 is the Greatest:",no3)
'''


no1 = int(input("\nEnter The No1 : "))
no2 = int(input("\nEnter The No2 : "))
no3 = int(input("\nEnter The No3 : "))


if no1 == no2 and no2 == no3 and no1 == no3:
    print("\nThree No's are same")
elif no1 == no2 and no1 != no3:
    if(no1>no3):
        print("\nNo1 and No2 are greater than No3")
    else:
        print("\nNo3 is greater than no1 and no3")
elif no1 == no3 and no1 != no2:
    if(no1>no2):
        print("\nNo1 and No3 are greater than No2")
    else:
        print("\nNo2 is greater than no1 and no3")

elif no2 == no3 and no1 != no2:
    if no2 > no1:
        print("\nno2 and no3 are greater than no1")
    else:
        print("\nno1 is greater than no1 and no3")

elif ((no1 != no2 and no2 != no3) and (no1 != no3)):
    if(no1>no2):
        if(no1>no3):
            print("\nno1 is max : ",no1)
        else:
            print("\nno3 is max : ",no3)

    else:
        if(no1>no3):
            print("\nno1 is max : ",no2)
        else:
            print("\nno3 is max : ",no3)
else:
    if(no2>no3):
        print("\nno2 is max : ",no2)
    else:
        print("\nno3 is max : ",no3)

