a = list(map(int, input().split()))
d = [[" "] * (len(a) + 2) for _ in range(max(a) + 2)]

for i in range(len(d)):
    d[i][0] = "*"
    d[i][len(d[0]) - 1] = "*"
for j in range(len(d[0])):
    d[0][j] = "*"

for j in range(len(a)):
    v = a[j]
    for i in range(len(d) - v, len(d)):
        d[i][j + 1] = "*" 

for line in d:
    print("".join(line))