# result = find_pairs([1, 2, 3, 4, 5, 6], 7)
# print(result)  # Output: [(3, 4), (2, 5), (1, 6)]

def find_pair(arr,tar):
    res = []
    sets = set()

    for no in arr:
        comp = tar - no
        if comp in sets:
            res.append((comp,no))
        sets.add(no)
        
    return res

res = find_pair([1,2,3,4,5,6,7],7)
print(res)


def find_pair(data,target):
    pairs = []
    for i in range(0,len(data)):
        for j in range(i+1,len(data)):
            if data[i] + data[j] == target:
                pairs.append((data[i],data[j]))
    return pairs

x = find_pair([1,2,3,4,5,6,7],2)
print(x)