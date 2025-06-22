'''
get name from user using input:
and give him 6 chnace to roll dice
and count how many times he got 6
use random


generate random name: 5 char
'''
import random
name = ""
for i in range(1,6):
    x = chr(random.randint(97,122))
    name = name+x
print(name)



data = [chr(i) for i in range(97,123)]

name1 = ""
for i in range(1,6):
    name1 += random.choice(data)

print(name1)


