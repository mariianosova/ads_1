cur = input()
p = float(input())
q = float(input())
n = int(input())
good = 1 if cur == "ясно" else 0
bad = 0 if cur == "ясно" else 1
for i in range(n):
    new_good = max(good * p, bad * (1 - q))
    new_bad = max(good * (1 - p), bad * q)
    good, bad = new_good, new_bad
if good > bad:
    print("ясно")
    print(good)
elif good == bad:
    print("равновероятно")
else:
    print("пасмурно")
    print(bad)