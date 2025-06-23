str = ["madam", "racecar", "python", "level", "world"]
palimdroms = {i: "yes" if i == i[::-1] else "no" for i in str}
print(palimdroms)


numbers = [121, 222, 34, 56, 789, 111, 90, 434]

palindromes = {i: "yes" if str(i) == str(i)[::-1] else "No" for i in numbers}
print(palindromes)
