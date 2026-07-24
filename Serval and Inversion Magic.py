t = int(input())

for _ in range(t):
  n = int(input())
  s = input()

  mismatched_blocks = 0
  in_block = False

  for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
      if not in_block:
        mismatched_blocks += 1
        in_block = True
    else:
      in_block = False

  if mismatched_blocks <= 1:
    print("Yes")
  else:
    print("No")
