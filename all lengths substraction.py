t = int(input())

for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))

  pos = a.index(n)
  possible = True

  for i in range(pos):
    if a[i] > a[i + 1]:
      possible = False
      break

  for i in range(pos, n - 1):
    if a[i] < a[i + 1]:
      possible = False
      break

  if possible:
    print("YES")
  else:
    print("NO")
