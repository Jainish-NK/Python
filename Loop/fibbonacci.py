no1 = 0
no2 = 1

print(no1,no2,end=" ")

for i in range(1,10):
    sum = no1 + no2
    print(sum,end=" ")
    no1 = no2
    no2 = sum

    