name = input("\nEnter The Name : ")

count = 0
for i in name:
    if " " in i:
        count += 1

print(count)
print("words ",count+1)
