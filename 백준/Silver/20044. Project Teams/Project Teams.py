n = int(input())
w = sorted(list(map(int,input().split())))
print(min([w[i] + w[-(i+1)] for i in range(n)]))