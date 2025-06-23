sales = ([10,20],[12,22],[10,12],[34,56],[100,200],[90,76],[90,90])
avgSalse = []
max = 0

for i,j in sales:
    if avgSalse[i][j] > max:
       max = avgSalse
       avg = (i+j)//2
       avgSalse.append(avg)
      
print(avgSalse)
