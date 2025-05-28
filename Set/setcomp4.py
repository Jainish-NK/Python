x = {i for i in range(1,11)}
print(x)

data =["bob","ram","racecar","parth","naman"]
palimdrom = {i for i in data if i == i[::-1]}
print(palimdrom)

cities = ["Ahmedabad","Surat","Anand","Rajkot","Somnath","Baroda"]

cities_set = {i[0] for i in cities}
print(cities_set)


cities1 = ["Ahmedabad","Surat","Anand","Rajkot","Somnath","Baroda","baroda","rajkot"]

set1 = {i.lower() for i in cities1}
print(set1)