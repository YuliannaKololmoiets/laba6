
S = input().strip()
l, r = map(int, input().split())
l = l-1
r= r-1

if l > r:
    substring = ""
else:
    substring = S[l:r+1]

prefixes = [substring[:i] for i in range(1, len(substring))]
print(len(prefixes)+2)
for p in prefixes:
    print(p)

