def findDuplicates(nums: list[int]) -> list[int]:
    result = []

    for num in nums:
        index = abs(num) - 1          # map value → index (1-indexed to 0-indexed)

        if nums[index] < 0:           # already flipped → seen before
            result.append(abs(num))
            
        else:
            nums[index] *= -1         # flip to mark as visited

    return result



# Why num - 1?

# array indices -> 0, 1, 2, 3
# array values  -> 1, 2, 3, 4

# So there is a gap of 1 between them:

# value 1 → index 0
# value 2 → index 1
# value 3 → index 2
# value 4 → index 3

# ==>To convert value to index, subtract 1. That's it.