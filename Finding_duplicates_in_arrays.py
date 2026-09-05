def findDuplicates(nums: list[int]) -> list[int]:
    result = []

    for num in nums:
        index = abs(num) - 1          # map value → index (1-indexed to 0-indexed)

        if nums[index] < 0:           # already flipped → seen before
            result.append(abs(num))
        else:
            nums[index] *= -1         # flip to mark as visited

    return result