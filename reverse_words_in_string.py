def reverse_words(s: str) -> str:
    # 1. split() breaks the string into a list of words, ignoring extra spaces
    words = s.split()
    
    # 2. words[::-1] reverses the list
    reversed_words = words[::-1]
    
    # 3. " ".join() connects the words with a single space
    return " ".join(reversed_words)






# --- Test Cases ---
if __name__ == "__main__":
    test_cases = [
        ("  the sky is blue  ", "blue is sky the"),
        ("hello world", "world hello"),
        ("  a good   example  ", "example good a"),
    ]
    
    for i, (s, expected) in enumerate(test_cases, 1):
        result = reverse_words(s)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test {i}: {status}")
        print(f"  Input:    '{s}'")
        print(f"  Expected: '{expected}'")
        print(f"  Got:      '{result}'\n")