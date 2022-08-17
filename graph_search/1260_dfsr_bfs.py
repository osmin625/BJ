from collections import deque
n, m, start = list(map(int,input().split(' ')))
graph = {key:[] for key in range(1,n+1)}
visited = [0] * (n + 1)
for _ in range(m):
    a,b = list(map(int,input().split(' ')))
    graph[a].append(b)
    graph[b].append(a)
for key in graph:
    graph[key]=sorted(graph[key])
# print(graph)
def dfs(node):
    visited[node]=1
    print(node,end=' ')
    for n in graph[node]:
        if visited[n] != 1:
            dfs(n)

def bfs(node):
    q = deque([node])
    visited[node]=1
    while q:
        n = q.popleft()
        print(n,end=' ')
        for i in graph[n]:
            if visited[i] != 1:
                q.append(i)
                visited[i]=1
                
dfs(start)
print()
visited = [0] * (n + 1)
bfs(start)