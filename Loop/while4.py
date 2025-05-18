'''
no = int(input("\nEnter The No : "))
sum=0
cube = 1
dup = no

while(no>0):
    temp = no%10
    cube = temp*temp*temp
    sum = sum + cube
    no = no // 10

if dup == sum:
    print(dup,"This No is Armstrong No")
else:
    print(dup,"This No is Not Armstrong No")


'''

no = int(input("\nEnter The no to Check Armstrong or not : "))
count = 0
dup1 = no
dup2 = no

while dup1 > 0:
    dup1 = dup1 // 10
    count+=1

print("\nNo of Digit : ",count)

temp = 0
sum = 0

while dup2 > 0:
    temp = dup2 % 10
    sum = sum + (temp**count)
    dup2 = dup2 // 10

print(sum)
if sum == no:
    print("armstrong no..")
else:
    print("not armstrong no...")
    