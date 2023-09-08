def yet_another_climbing(x, y):
  if x == 0:
    return 0
  elif x < y:
    return x
  else:
    return 1 + yet_another_climbing(x - y, y)


t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(yet_another_climbing(x, y))
