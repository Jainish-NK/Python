import random
x = random.random()
#print(x)

x1 = random.randint(1,100)
#print(x1)

x2 = random.uniform(1,10)
#print(x2)

data = ["ram","shyam","amit","sumit"]
name = random.choice(data)
print(name)

random.shuffle(data)
print(data)

random.seed(5)
print(random.randint(1,100))
