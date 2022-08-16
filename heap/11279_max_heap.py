import sys
input = sys.stdin.readline
h = [0]

def insert(x):
    h.append(x)
    idx = len(h) - 1
    while idx != 1:
        if h[idx // 2] < h[idx]:
            h[idx // 2], h[idx] = h[idx], h[idx // 2]
        idx = idx // 2
def delete(x):
    h[1], h[-1] = h[-1], h[1]
    print(h.pop())
    n = 1
    while (1):
        if len(h) > 2 * n + 1:
            if max(h[n], h[2 * n], h[2 * n + 1]) == h[2 * n]:
                h[n], h[2 * n] = h[2 * n], h[n]
                n *= 2
            elif max(h[n], h[2 * n], h[2 * n + 1]) == h[2 * n + 1]:
                h[n], h[2 * n + 1] = h[2 * n + 1], h[n]
                n = n * 2 + 1
            else:
                break
        elif len(h) > 2 * n and max(h[n], h[2 * n]) == h[2 * n]:
            h[n], h[2 * n] = h[2 * n], h[n]
            break
        else:
            break

N = int(input().rstrip())
for _ in range(N):
    x = int(input().rstrip())
    if x:
        insert(x)
    elif len(h) > 1:
        delete(x)
    else:
        print(0)