# Rotate a list to the right by k steps.

# Input: [1, 2, 3, 4, 5], k=2
# Output: [4, 5, 1, 2, 3]

k= 2
data = [1,2,3,4,5]

length = len(data)
k = k%length

x = data[-k:] + data[:-k]

print(x)