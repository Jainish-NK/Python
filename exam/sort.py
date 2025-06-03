def get_sec_ele(t):
    return t[1]

data = [(1,20),(3,15),(2,50),(4,10),(5,30)]

sorted_data = sorted(data,key=get_sec_ele,reverse=True)

print(sorted_data)