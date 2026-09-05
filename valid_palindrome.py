def is_palindrome(sentence: str) -> bool:
    left = 0
    right = len(sentence) - 1


# sentence[left] -> give me the character at position left inside the string sentence

    while left < right:  # keep comparing pairs until pointers cross
        while left < right and not sentence[left].isalnum():
            left += 1  # this character is junk (space/punctuation), skip it and check the next one

        while left < right and not sentence[right].isalnum():
            right -= 1

        if sentence[left].lower() != sentence[right].lower():
            return False

# These actually move the pointers
        left += 1
        right -= 1

    return True











# --- Test Cases ---
if __name__ == "__main__":
    test_cases = [
        ("Tenet", True),
        ("Teneter", False),
    ]
    
    for i, (s, expected) in enumerate(test_cases, 1):
        result = is_palindrome(s)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test {i}: {status}")
        print(f"  Input:    '{s}'")
        print(f"  Expected: {expected}")