no = 123
temp = 0
sum = 0


while no>0:
    temp = no%10
    sum += temp
    no = no // 10

print("Sum : ",sum)

