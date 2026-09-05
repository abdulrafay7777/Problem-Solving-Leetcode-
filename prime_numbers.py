import math

def generate_primes(n: int) -> list[int]:
    # Edge case: there are no primes less than 2
    if n < 2:
        return []
        
    primes = []
    
    for num in range(2, n + 1):
        is_prime = True
        
        # We only need to check divisors up to the square root of the number
        limit = math.isqrt(num)
        
        for i in range(2, limit + 1):
            if num % i == 0:
                is_prime = False
                break  # Not prime, stop checking
                
        if is_prime:
            primes.append(num)
            
    return primes









# --- Test Cases ---
if __name__ == "__main__":
    test_cases = [
        (10, [2, 3, 5, 7]),
        (20, [2, 3, 5, 7, 11, 13, 17, 19]),
        (1, []),
        (2, [2]),
        (30, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    ]
    
    for idx, (n, expected) in enumerate(test_cases, 1):
        result = generate_primes(n)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test {idx}: {status}")
        print(f"  Input:    {n}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}\n")