import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
cnt = 0
for w in words:
    if len(w) % 2:
        pass
    else:
        stack = []
        for i in w:
            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        if not stack:
            cnt += 1
print(cnt)