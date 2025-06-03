num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,121,132,45,65,54,85]

def even_numbers(data):
    for i in data:
        if i%2==0:
            yield i

x = even_numbers(num)
# print(next(x))
# print(next(x))
# print(next(x))

for i in x:
    print(i)