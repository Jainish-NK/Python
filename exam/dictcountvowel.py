str = input("Enter The Sentence : ")
words = str.split()
vowels = "aeiouAEIOU"
res = {}


for word in words:
    count = 0
    for ch in word:
        if ch in vowels:
            count += 1
    res[word] = count

print(res)    