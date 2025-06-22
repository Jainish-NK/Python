# Use sets to find elements common in both lists.

# Input: [1, 2, 3], [2, 3, 4]
# Output: {2, 3}

l1 = set([1,2,3])
l2 = set([2,3,4])

ans = l1.intersection(l2)
print(ans)