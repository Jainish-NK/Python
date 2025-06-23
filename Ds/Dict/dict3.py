

data = {1:100,2:34,3:23,4:121,5:44}
filtDict ={}

for i,j in data.items():
    if j %2 ==0:
        filtDict[i]=j

print(filtDict)   

