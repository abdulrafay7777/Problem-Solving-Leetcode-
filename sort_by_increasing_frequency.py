def frequency_sort(nums):
    # ── Step 1: Manual frequency count (no Counter) ──────────────────────────
    freq = {}
    for n in nums:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1

    # ── Step 2: Get unique values (no set()) ─────────────────────────────────
    seen = {}
    unique = []
    for n in nums:
        if n not in seen:
            seen[n] = True
            unique.append(n)

    # ── Step 3: Manual bubble sort on unique values ───────────────────────────
    #    Primary key:   higher frequency first
    #    Secondary key: smaller number first (tiebreaker)
    n = len(unique)
    for i in range(n):
        for j in range(0, n - i - 1):
            a, b = unique[j], unique[j + 1]
            should_swap = (
                freq[a] < freq[b] or          # b has higher freq → swap
                (freq[a] == freq[b] and a > b) # same freq, a is bigger → swap
            )
            if should_swap:
                unique[j], unique[j + 1] = unique[j + 1], unique[j]

    # ── Step 4: Reconstruct result ────────────────────────────────────────────
    result = []
    for num in unique:
        for _ in range(freq[num]):
            result.append(num)

    return result


# ── Tests ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    cases = [
        ([1, 1, 2, 2, 2, 3], [2, 2, 2, 1, 1, 3]),
        ([4, 4, 1, 1, 2],    [1, 1, 4, 4, 2]),
        ([5, 5, 4, 6, 4],    [4, 4, 5, 5, 6]),
    ]

    for inp, expected in cases:
        result = frequency_sort(inp)
        status = "✓" if result == expected else "✗"
        print(f"{status}  Input:    {inp}")
        print(f"   Expected: {expected}")
