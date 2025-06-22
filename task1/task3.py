# Return all elements that appear more than once.

# Input: [4, 3, 2, 7, 8, 2, 3, 1]
# Output: [2, 3]

nums = [4, 3, 2, 7, 8, 2, 3, 1]
duplicates = []

for i in range(len(nums)):
    if nums[i] not in duplicates and nums[i] in nums[i+1:]:
        duplicates.append(nums[i])

print(duplicates)  # ➞ [2, 3]
