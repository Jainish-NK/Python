s = "Hello World"
vowel = consonant = 0
vowel = ['a','e','i','o','u','A','E','I','O','U']

for i in s:
    if ('a'<=i<='z') or ('A'<=i<='Z'):
        if i in vowel:
          vowel+=1
        else:
           consonant+=1

print(vowel)
print(consonant)