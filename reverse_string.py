def reverseString(s: list[str]) -> None:
    #left, right = 0, len(s) - 1

    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left] #swapping OR use temp variable

        left += 1  # Moving inward
        right -= 1


# Returns list[str] —> makes a new one 
# Returns None —> modifies original / changes the original


        # s = ["h", "e", "l", "l", "o"]

# Grab the first and last person → swap their cards → move inward → repeat