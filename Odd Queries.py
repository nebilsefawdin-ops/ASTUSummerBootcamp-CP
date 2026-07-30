for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    
    p = [0]
    for x in a:
        p.append(p[-1] + x)
        
    for _ in range(q):
        l, r, k = map(int, input().split())
        
        ans = p[-1] - (p[r] - p[l - 1]) + (r - l + 1) * k
        
        if ans % 2 == 1:
            print("YES")
        else:
            print("NO")
