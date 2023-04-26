n = int(input())
a = set()
for _ in range(n):
    a.add(input())
m = int(input())
ans = []
for _ in range(m):
    name = input()
    k = int(input())
    f = True
    for _ in range(k):
        data = input()
        if data not in a:
            f = False
    if f:
        ans.append(name)
for elem in ans:
    print(elem)