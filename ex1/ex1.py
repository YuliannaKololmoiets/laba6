def process_suffixes(s, l, r):
    substring = s[l:r + 1] if l <= r else ""
    n = len(substring)

    print(n + 1)

    for i in range(1, n):
        print(substring[i:])

    print("")

s = input().strip()
l, r = map(int, input().split())

process_suffixes(s, l-1, r-1)

