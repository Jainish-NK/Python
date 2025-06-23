data = ["ram","shyam","amit","kunal","amit","ram","amit","ajay"]

flag = -1

for i in range(len(data)):
    if data[i] == "ram":
        flag = i
        break #find first occurence of ram
print(flag)

#ind1 = data.index("amit") #2
ind1 = data.index("amit",3)
print("index..",ind1)

print(data.count("ram"))
print(data.count("amit"))