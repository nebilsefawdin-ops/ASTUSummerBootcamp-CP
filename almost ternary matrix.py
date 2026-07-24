t = int(input())

for _ in range(t):
  n, m = map(int, input().split())

  for i in range(n):
    row = []
    for j in range(m):
      if (i % 4 in [0, 3]) == (j % 4 in [0, 3]):
        row.append("1")
      else:
        row.append("0")
    print(" ".join(row))
