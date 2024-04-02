'''
dp
끝이 삼각형인 경우
끝이 마름모인 경우
'''
def solution(n, tops):
    mem = [[0, 0] for _ in range(n)]
    if tops[0]:
        mem[0] = [3, 1]
    else:
        mem[0] = [2, 1]
    for i in range(1,n):
        before_ = sum(mem[i-1])
        mem[i][0] = (mem[i-1][0] + before_ * (1 + tops[i])) % 10007
        mem[i][1] = before_ % 10007

    return sum(mem[i]) % 10007