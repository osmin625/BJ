N, K = map(int,input().split())
num = list(map(int,list(input())))
# print(num)
stack = []
for n in num:
    while stack:
        if K and stack[-1] < n: # cursor의 숫자가 n보다 작으면
            stack.pop()
            K -= 1
        else:
            break
    stack.append(n)
while K:
    stack.pop()
    K -= 1
print(*stack, sep='')