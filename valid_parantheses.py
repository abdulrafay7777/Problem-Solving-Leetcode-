def isValid(s: str) -> bool:
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in matching:                    # is closing bracket?
            if not stack or stack[-1] != matching[char]:
                return False
            
            stack.pop()

        else:                                   # opening bracket
            stack.append(char)
    
    return len(stack) == 0


# Openers go IN to the stack first, then closers come and KICK THEM OUT one by one — if everything pairs up correctly, stack ends empty.

# Stack follows LIFO

# stack[-1]  →  '['   # last element  
# stack[-2]  →  '{'   # second to last



# CREATE an empty stack (a pile where we store opening brackets)
# CREATE a cheat sheet that maps each closing bracket to its expected opener:
#     ')' should be paired with '('
#     '}' should be paired with '{'
#     ']' should be paired with '['

# LOOK at each character in the string one by one:

#     IF the character is a closing bracket ) } ]
    
#         CHECK two things:
#             1. Is the stack empty?        (nothing was opened before this)
#             2. Does the top of stack NOT match the expected opener?
        
#         IF either of those is true:
#             RETURN False  (invalid, stop immediately)
        
#         OTHERWISE:
#             Remove the top from the stack  (this pair is matched, done with it)
    
#     IF the character is an opening bracket ( { [
    
#         Push it onto the stack  (save it, wait for its closing partner)

# AFTER scanning every character:

#     IF stack is empty   → every opener got matched → RETURN True  ✅
#     IF stack has items  → some openers never closed → RETURN False ❌