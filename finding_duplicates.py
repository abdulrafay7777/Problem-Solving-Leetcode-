def find_duplicates(nums: list[int]) -> list[int]:
    seen = set()
    duplicates = set()
    
    for num in nums:
        # If we've seen this number before, it's a duplicate
        if num in seen:
            duplicates.add(num)
        else:
            # Otherwise, mark it as seen
            seen.add(num)
            
    # Convert the set of duplicates back to a list before returning
    return list(duplicates)





# --- Test Cases ---
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 1, 2, 5], [1, 2]),
        ([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]),
        ([1, 1, 1, 1], [1]),
        ([1, 2, 3], []),
    ]
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = find_duplicates(nums)
        
        # Since order doesn't matter, we sort both lists before comparing
        status = "PASSED" if sorted(result) == sorted(expected) else "FAILED"
        print(f"Test {i}: {status}")
        print(f"  Input:    {nums}")
        print(f"  Expected: {expected} (in any order)")