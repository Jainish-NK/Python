numbers = [1,2,3,4,5]
#sq_numbers = [i**2 for i in numbers]
#sq_numbers = map(lambda x : x**2,numbers)
#sq_numbers = list(map(lambda x : x**2,numbers))
#sq_numbers = tuple(map(lambda x : x**2,numbers))
sq_numbers = set(map(lambda x : x**2 , numbers))
print(sq_numbers)


name = "ahmedabad"
upper_name = map(lambda x : x.upper(),name)
print(list(upper_name))

data = ["amit","sumit","jay","raj","parth","kunal","smit","sanjay"]
upper_list = list(map(lambda x : x.upper(),data))
print(upper_list)

