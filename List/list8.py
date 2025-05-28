data =["ram","shyam","ram","seeta","seeta","ajay"]
uniqueElm = []
duplicate = []


#data =["ram","shyam","ram","seeta","seeta","ajay"] 
#duplicate elem
#out["ram","seeta"]

for i in data:
    if i not in uniqueElm:
        uniqueElm.append(i)
    else:
        duplicate.append(i)

print(uniqueElm)
print(duplicate)