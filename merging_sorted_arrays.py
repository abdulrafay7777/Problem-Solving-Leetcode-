def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    merged = []
    i = 0  # Pointer for arr1
    j = 0  # Pointer for arr2

    # arr1 = [1, 3, 5, 7]
    # arr2 = [2, 4, 6, 8]
    
    # Compare elements from both arrays and add the smaller one to merged
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
            
    # Once one array is exhausted, add any remaining elements from the other.
    # We use slicing here, but you could also use another while loop.
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    
    return merged







# --- Test Cases ---
if __name__ == "__main__":
    test_cases = [
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 5, 9], [2, 3, 4, 6], [1, 2, 3, 4, 5, 6, 9]),
        ([], [1, 2], [1, 2]),
        ([1, 2], [], [1, 2])
    ]
    
    for idx, (arr1, arr2, expected) in enumerate(test_cases, 1):
        result = merge_sorted_arrays(arr1, arr2)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test {idx}: {status}")
        print(f"  Input:    arr1 = {arr1}, arr2 = {arr2}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}\n")