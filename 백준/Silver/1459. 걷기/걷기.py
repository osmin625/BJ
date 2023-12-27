X, Y, W, S = map(int, input().split())


def solution(x, y, w, s):
    if w * 2 <= s:
        return w * (x + y)
    if w < s:
        return min(x,y) * s + abs(x-y) * w
    if not (x + y) % 2:
        return max(x,y) * s
    else:
        return (max(x,y)-1) * s + w


print(solution(X, Y, W, S))
