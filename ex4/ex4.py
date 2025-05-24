n = int(input())
z = list(map(int, input().split()))

p = [0] * n

for i in range(1, n):
    for j in range(z[i]):
        if i + j < n:
            p[i + j] = max(p[i + j], j + 1)
        else:
            break

print(*p)

