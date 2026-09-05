def two_sum(nums: list[int], target: int) -> list[int]:
    # Dictionary to store the numbers we've seen and their indices
    # Format: {number: index}
    seen = {}   #--> seen = {2: 0, 7: 1}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # If the complement exists in our dictionary, we found the pair!
        if complement in seen:
            return [seen[complement], i]
            
        # Otherwise, add the current number and its index to the dictionary
        seen[num] = i    # seen[2] = 0
        
    return [] # Fallback, though the constraints guarantee a solution



# num + ? = target
# ? = target - num

# ----------------------
# Complement = What is missing to make something complete?

# Whatever you search/lookup by → that MUST be the key

# seen[complement] doesn't return the number, it returns the index of that number. That's the whole point of storing {number: index}
# i -> index of current number 



# --- Test Cases ---
if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = two_sum(nums, target)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test {i}: {status}")
        print(f"  Input:    nums = {nums}, target = {target}")
        print(f"  Expected: {expected}")


        # nums = [2, 7, 11, 15], target 9




# 1. I need a notebook to remember numbers I've seen
# 2. Visit each number one by one
# 3. Calculate what I need (target - current)
# 4. Check notebook if I've seen it
# 5. Yes → return both indexes
# 6. No  → write current in notebook