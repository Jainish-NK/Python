#{key : value for in items}

#{0:0,1:1,2:4,3:9,4:16,5:25}

data ={i:i**2 for i in range(6)}
print(data)

data = {i:i**2 for i in range(10) if  i %2 ==0}
print(data)


fruits = ["apple", "banana", "cherry"]

fruits_len = {f:len(f) for f in fruits}
print(fruits_len)

