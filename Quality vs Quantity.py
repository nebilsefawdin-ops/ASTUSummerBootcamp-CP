t=int(input())

for i in range (t):
    n=int(input())
    a=list(map(int,input().split()))

    a.sort()

    blue_sum=a[0]+a[1]
    red_sum=a[-1]

    i=2
    j=n-2

    ans="NO"

    while i <= j:
        if red_sum > blue_sum:
            ans="YES"
            break
        blue_sum += a[i]
        red_sum +=a[j]

        i += 1
        j -= 1
    if red_sum > blue_sum :
        ans="YES"
    print(ans)
