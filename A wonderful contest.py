t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = {}

    for x in a:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    ok = False
    for x in freq:
        if freq[x] == 1:
            ok = True
            break

    print("YES" if ok else "NO")