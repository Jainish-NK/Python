name = input("\nEnter The Name : ")
res = ""

for i in name:
    if not ('0'<= i <= '9'):
        res+=i
    
print("Without Digit : ",res)