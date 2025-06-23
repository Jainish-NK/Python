days = {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday"}
print(days)

removeValue = days.pop(2) #tuesday
print("removing...",removeValue)
print(days)

x = days.popitem() #last item
print("removing...",x)
print(days)

print(days.get(1)) #Monday