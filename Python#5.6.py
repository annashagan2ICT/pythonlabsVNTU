a = list(map(int, input().split()))

pos = 0
for i in range(len(a)):
    if a[i] != 0:
        a[pos], a[i] = a[i], a[pos]
        pos += 1

print(a)