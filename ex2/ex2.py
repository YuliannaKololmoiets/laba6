def match_from_position(P, T, k):
    comparison_count = 0
    match = True

    if k + len(P) > len(T):
        print("NO")
        print(len(P))
        return

    for i in range(len(P)):
        comparison_count += 1
        if P[i] != T[k + i]:
            match = False
            break
        

    print("YES" if match else "NO")
    print(comparison_count)

P = input().strip()
T = input().strip()
k = int(input())

match_from_position(P, T, k-1)
