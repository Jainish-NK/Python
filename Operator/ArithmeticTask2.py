#Without Using Third Variable
no1 = 100
no2 = 200

no1 = no1+no2
no2 = no1-no2
no1 = no1-no2

print("no1 = ",no1)
print("no2 = ",no2)


#Using Third Variable 
no1 = 100
no2 = 200

temp = no1
no1 = no2
no2 = temp

print(no1,no2)
#print("no1 = ",no1)
#print("no2 = ",no2)