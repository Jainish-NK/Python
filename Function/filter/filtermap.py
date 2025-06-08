num = [1,2,3,4,5,6,7,8,9,10]
num = range(1,11)

#ans = filter(lambda x : x>30,nums)
ans = filter(lambda x : x>30,map(lambda x : x**2 ,num))
print(list(ans))

data = ["amit","sumit","jay","raj","parth","kunal","smit","sanjay"]

ans1 = filter(lambda x : x.startswith('S'),map(lambda x : x.upper(),data))
print(list(ans1))