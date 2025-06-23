sales = ([10,20],[12,22],[10,12],[34,56],[100,200],[90,76],[90,90])
avgSales = []

for i,j in sales:
    avg = (i+j) //2
    avgSales.append(avg)
print(avgSales)

maxValue = max(avgSales)
print("max value....",maxValue)

ind = avgSales.index(maxValue)
print("index ",ind+1)

d1 = ("ram","shyam","amit","hariram","ajay")

#maxValue2 = max(d1,key=len)
maxValue2 = max(d1)
print(maxValue2)