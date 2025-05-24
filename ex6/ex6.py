def max_block_length(s):
    n = len(s)
    max_len = 0

    for k in range(1, n):
        length = 0
        for i in range(n - k):
            if s[i] == s[k + i]:
                length += 1
            else:
                break
        max_len = max(max_len, length)
    
    return max_len

s = input().strip()

print(max_block_length(s))

