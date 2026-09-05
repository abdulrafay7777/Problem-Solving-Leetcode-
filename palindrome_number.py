class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negatives are not palindromes
        # Numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        extracted = 0
        
        while x > extracted:
            # I want to attach the last digit of x to the right side of reversedHalf

            # × 10 just creates an empty slot for the next digit
            extracted = extracted * 10 + x % 10  # 1
            x //= 10 # just deletes the digit you already used.
        
        # Even digits: x == extracted
        # Odd digits:  x == extracted // 10  (middle digit doesn't matter)
        return x == extracted or x == extracted // 10










# Case 1 — Even digits: 1221

# Start:   x = 1221,  reversedHalf = 0

# Step 1:  x = 122,   reversedHalf = 1
# Step 2:  x = 12,    reversedHalf = 12   ← STOP (12 > 12 is false)

# x = 12   (left half)
# reversedHalf = 12   (right half reversed)

# -------------------------------------------------

# Case 2 — Odd digits: 12321
# Start:   x = 12321,  reversedHalf = 0

# Step 1:  x = 1232,   reversedHalf = 1
# Step 2:  x = 123,    reversedHalf = 12
# Step 3:  x = 12,     reversedHalf = 123  ← STOP (12 > 123 is false)

# x = 12    (left half)
# reversedHalf = 123  (right half reversed — but includes MIDDLE digit!)

# The middle digit 3 is stuck inside reversedHalf. You need to throw it away:

# reversedHalf // 10 = 123 // 10 = 12

# x == reversedHalf // 10
# 12 == 12  ✅