import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = {key:[] for key in range(1,N+1)}
visited = [0 for _ in range(1000+1)]
stack = []
cc = 0
for i in range(M):
    n1, n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
for i in range(1,N+1):
    if not visited[i]:
        cc += 1
        stack.append(i)
        while stack:
            node = stack.pop()
            for n in graph[node]:
                if not visited[n] and n not in stack:
                    stack.append(n)
            visited[node] = 1
print(cc)