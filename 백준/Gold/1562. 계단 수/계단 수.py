# 계단 수
# 0~9까지 모두 등장하는 계단 수
# 0으로 시작하지 않음.
# 단순하게 생각하면 bf문제.
# 중간 지점들을 경유하는 계산이 중복될 수 있다는 점에서 메모이제이션 필요.
# dp 문제.

# 메모이제이션에 필요한 정보
# 1. 현재까지 사용된 숫자
# 3. 현재 위치까지 왔을 때의 경우의 수(max)
#       이전 경우(좌,우)중 더 큰 값 + 1

# 여기서 현재 위치를 기록하는 것을 놓쳤다.
# 현재 위치까지 필요하기 때문에 3차원 배열이 필요하다.
# 방문한 수에 따라 경우의 수를 기록하기 위해 dict를 써야할 것 같다.
# defaultdict를 쓰자.
# 아닌 것 같다. 3차원 배열을 다시 쓰자.

MAX_VAL = 1000000000

N = int(input())
mem = [[[0 for _ in range(2 ** 10)] for _ in range(10)] for _ in range(N)]
for pos in range(1,10): # 0으로 시작하면 계단 수가 될 수 없음.
    mem[0][pos][(1 << pos)] = 1
for i in range(1, N):
    for pos in range(10):
        for flag in range(2 ** 10):
            next_ = int(bin(flag | (1 << pos)), 2)
            # print(next_)
            if pos > 0:
                mem[i][pos][next_] += mem[i - 1][pos - 1][flag] % MAX_VAL
            if pos < 9:
                mem[i][pos][next_] += mem[i - 1][pos + 1][flag] % MAX_VAL

print(sum([mem[N - 1][i][(1 << 10) - 1] for i in range(10)]) % MAX_VAL)
