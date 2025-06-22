# read data from file.....
# file has data like this
# bob
# john
# ram
# shyam
# naman
# parth
# madam
# java
# python

# Read data from file
with open("./File/notpalimdrom.txt", "r") as file:
    data = file.read().splitlines()  # or file.readlines() and strip each line

# Write palindromes to new file
with open("./File/palimdrom1.txt", "w") as file:
    for word in data:
        word = word.strip()  # remove extra spaces or \n
        if word == word[::-1]:  # check if it's a palindrome
            file.write(word + "\n")
