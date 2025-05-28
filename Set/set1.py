data = set({})
print(data)

data = {10,20,30,40,50,60,10,30}
print(data)
print(type(data))

#print(data[0]) #error

data.add(500)
data.update({77,66,55,44}) #extend
data.update("java")
print(data)

#remove...

#data.clear()    #emprt set
removeEle = data.pop() #len check..
print("removeing...",removeEle)

data.remove(600) #error if not present
#data.discard(600) #no error if not present
print(data)