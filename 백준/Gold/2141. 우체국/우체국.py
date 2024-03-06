import sys
input = sys.stdin.readline
n = int(input())
town, people = [], 0
for i in range(n):
    a, b = map(int,input().split())
    town.append((a,b))
    people += b

town.sort()
cnt = 0
for i in range(n):
    cnt += town[i][1]
    if cnt >= people / 2:
        print(town[i][0])
        break
