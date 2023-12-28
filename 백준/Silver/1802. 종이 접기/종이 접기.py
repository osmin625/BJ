import sys
input = sys.stdin.readline


def is_symmetric(m):
    lm = len(m)
    if lm == 1:
        return True
    if lm == 3:
        if m[0] != m[-1]:
            return True
        return False
    if all([m[i] != m[-1 * (i + 1)] for i in range(lm // 2)]):
        return is_symmetric(m[: lm // 2]) and is_symmetric(m[lm // 2 + 1:])
    return False


for _ in range(int(input())):
    paper = input().rstrip()
    print('YES') if is_symmetric(paper) else print('NO')