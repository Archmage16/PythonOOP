x1, x2, x3 = map(int, input().split())
total = [x1, x2, x3]
total.sort()
s = 0
for i in range(total[0],total[2]):
    s += 1
for i in range(total[2], total[0], -1):
    s += 1
print(s)