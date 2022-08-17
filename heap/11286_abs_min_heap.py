import sys
input = sys.stdin.readline

h = [0]
def insert(x):
    h.append((abs(x),x))
    idx = len(h) -1
    while idx != 1:
        if h[idx//2][0] > h[idx][0]:
            h[idx//2],h[idx] = h[idx],h[idx//2]
        elif h[idx//2][0] == h[idx][0] and h[idx//2][1] > h[idx][1]:
            h[idx//2],h[idx] = h[idx],h[idx//2]
        idx //= 2
def pop(x):
    if len(h) == 1:
        print(0)
        return
    h[1], h[-1] = h[-1],h[1]
    print(h.pop()[1])
    i = 1
    while True:
        if len(h) > 2 * i + 1:
            t = sorted([h[i],h[2 * i],h[2 * i + 1]],key = lambda x:(x[0], x[1]))
            if t[0] == h[2 * i]:
                h[i], h[2 * i] = h[2 * i],h[i]
                i *= 2
            elif t[0] == h[2 * i + 1]:
                h[i], h[2 * i + 1] = h[2 * i + 1],h[i]
                i = i * 2 + 1
            else:
                break
        elif len(h) > 2 * i:
            t = sorted([h[i],h[2 * i]],key = lambda x:(x[0], x[1]))
            if t[0] == h[2 * i]:
                h[i], h[2 * i] = h[2 * i],h[i]
        else:
            break
N = int(input())
for _ in range(N):
    x = int(input())
    if x:
        insert(x)
    else:
        pop(x)