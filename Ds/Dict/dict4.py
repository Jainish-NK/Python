data = {"ram":"ram","shyam":"shyam","sumit":"sumit","amit":"amit","parth":"parth","aba":"aba"}
data1 = {}

for i, j in data.items():
    if len(j) > 5:
        data1[i] = j
    elif j.startswith("G"):
        data1[i] = j
    elif j == j[::-1]:  # Correct: Check if value is palindrome
        data1[i] = j

print(data1)

data = {"cricket":"seema","football":"dharmaraj","rugby":"sus","volleyball":"het"}

data1={}

for i,j in data.items():
    if j.startswith("s") or len(j) > 5 or j == j[::-1]:
        data1[i] = j
print(data1)


