def palindrome(x: int) -> bool:

    if x < 0 or (x % 10 and x != 0):
        return False

    extracted = 0

    while x > extracted:
        extracted = extracted * 10 + x % 10
        x //= 10 

    return x == extracted or x == extracted // 10