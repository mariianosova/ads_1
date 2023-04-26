value = input()

ans = set()
last = set()
deleted = {}
while value:
    value = int(value)
    if value == -1:
        for elem in last:
            if elem in ans:
                deleted[elem] = True
                ans.remove(elem)
            elif elem not in deleted:
                ans.add(elem)
        last = set()
    else:
        last.add(value)

    value = input()

print(*ans)