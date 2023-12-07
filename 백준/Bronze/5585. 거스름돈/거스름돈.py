ans = 0
money = 1000 - int(input())
for c in [500, 100, 50, 10, 5, 1]:
    ans += money // c
    money %= c
print(ans)