numbers = [1,2,3,4,5]

x = ["even" if i %2==0 else "odd" for i in numbers]
print(x)

data = ["ram","","shyam",None,"amit"]

x1 = [i for i in data if i]
print(x1)

number = [-1,-2,-3,4,5,6]

x2 = ["positive" if i>0 else "negative" for i in number]
print(x2)