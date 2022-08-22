import sys
input = sys.stdin.readline
lst = [1,3,5]
lst.extend([0 for _ in range(997)])
for i in range(3,1000):
    lst[i] = lst[i - 1] + 2 * lst[i - 2]
print(lst[int(input())-1] % 10007)