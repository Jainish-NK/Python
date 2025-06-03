int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
count = 0

for i in int_list:
    if i%2 == 0:
        even_list.append(i)
        count = len(even_list)

print(even_list)
print("Count of even numbers:", count)

    