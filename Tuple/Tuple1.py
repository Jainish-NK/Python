#[] , ()

#data = ()
data = ("ram","shyam","sumit","amit","parth")
#print(data)
print(type(data))

#data[0] = "RAM" TypeError: 'tuple' object does not support item assignment
print(data)

cnt = data.count("ram")
print(cnt)

ind = data.index("shyam")
print(ind)

for i in data:
    print(i)