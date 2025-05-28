#data = {}
data = {"Gujarat":"Gandhinagar","Bihar":"Patna","UP":"Lucknow"}
print(data)
print(type(data))

print(data["Gujarat"])

data["WB"] = "Kolkata" #at time one key value pair add...
data["Gujarat"] = "Ahmedabad" #update value of key
print(data)

#add multiple data
data.update({"Tamilnadu":"chennai","Kerala":"Trivandrum"})

k = data.keys()
print(k)
v = data.values()
print(v)

kv = data.items()
print(kv)

for i , j in data.items():
    print(i,":",j)

    