name = input("\nEnter the name: ")
vowel = 0
consonant = 0

# Manual list of vowels (both small and capital)
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for i in name:
    # Check if character is an alphabet (A-Z or a-z)
    if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
        if i in vowels:
            vowel += 1
        else:
            consonant += 1

print(vowel, "number of vowels")
print(consonant, "number of consonants")
