import sys
input = sys.stdin.readline

def num_same(n):
    num_list = [n]
    temp = n * n % 10
    while temp != n:
        num_list.append(temp)
        temp = temp * n % 10
    return num_list
for _ in range(int(input())):
    a,b = map(int,input().split())
    temp = num_same(a % 10)
    result = temp[b % len(temp) - 1]
    if result:
        print(temp[b % len(temp) - 1])
    else:
        print(10)
