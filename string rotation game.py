t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    blocks = 1
    has_same = False

    for i in range(1, n):
        if s[i] != s[i - 1]:
            blocks += 1
        else:
            has_same = True

    if s[0] == s[-1] or not has_same:
        print(blocks)
    else:
        print(blocks + 1)