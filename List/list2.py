sales = [100,23,45,678,900,333,234,765]
print(sales)

removedlm = sales.pop() #last index if list empty IndexError : pop from empty list
#removedlm = sales.pop(3)  #specific index IndexError : pop index out of range
print("removing....",removedlm)
print(sales)

#remove...

sales.remove(900)
print(sales)

#for i in sales:
#    print(i)
