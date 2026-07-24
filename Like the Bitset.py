t = int(input())

for _ in range(t):
  n, k = map(int, input().split())
  s = input()

  max_ones = 0
  current_ones = 0

  for char in s:
    if char == "1":
      current_ones += 1
      if current_ones > max_ones:
        max_ones = current_ones
    else:
      current_ones = 0

  if max_ones >= k:
    print("NO")
  else:
    print("YES")
    p = []
    small = 1
    large = n

    for char in s:
      if char == "1":
        p.append(small)
        small += 1
      else:
        p.append(large)
        large -= 1

    print(" ".join(p))
