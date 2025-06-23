firstName = ["ram","shyam","sita","amit"]
lastName = ["sharma","prashad","patel"]

#fullName = [f"{f} {l}" for f in firstName for l in lastName]
fullName = [f"{firstName[i]} {lastName[j]}"for i in range(len(firstName)) for j in range(len(lastName))]
print(fullName)
