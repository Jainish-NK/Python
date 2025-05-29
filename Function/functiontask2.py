def findMax(*args):
    return max(args)

ans = findMax(10,8,563,7827,365)
print("ans = ",ans)



def chek_threshold(th,*args):
    return [i for i in args if i>th]

print(chek_threshold(200,900,560,80,67,121,201))

# ans = chek_threshold(200,900,560,80,67,121,201)
# print(ans)