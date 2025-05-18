name = "Jainish khunt"
print(name)

#immutable 
#name[0] = "J" #TypeError: 'str' object does not support item aasignment

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])

#string lenth find..

length = len(name)
print("length ",length)

#for i in range(0,length):
#for i in range(0,len(name)):
for i in range(len(name)):
    print(name[i])

#print(name)

x = 65
print("chr...",chr(x))

y = 'a'
print("y..",ord(y))