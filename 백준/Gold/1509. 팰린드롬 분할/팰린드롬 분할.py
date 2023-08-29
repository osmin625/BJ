import sys

input = sys.stdin.readline

line = list(input().rstrip())
N = len(line)
pal_table = [[0 for _ in range(N)] for _ in range(N)]

# 길이 1인 경우 팰린드롬
for i in range(N):
    pal_table[i][i] = 1

# 길이 2인 경우의 팰린드롬
for i in range(N - 1):
    if line[i] == line[i + 1]:
        pal_table[i][i + 1] = 1

# 길이 l인 경우의 팰린드롬 (l > 2)
for l in range(N - 2):  # 팰린드롬의 길이가 l인 경우
    for start in range(N - 2 - l):  # 시작지점 start
        # 기존의 팰린드롬 바깥 양쪽의 문자열이 서로 동일하면 팰린드롬.
        end = start + l + 2
        # if 팰린드롬인가? and 추가된 양 끝의 문자열이 동일한가?
        if pal_table[start + 1][end - 1] and line[start] == line[end]:
            pal_table[start][end] = 1
# print(*pal_table, sep='\n')

m = [0 for _ in range(N)]
m[0] = 1

for i in range(1, N):
    min_val = m[i - 1] + 1
    for j in range(i): 
        if pal_table[j][i]: # i로 끝나는 팰린드롬이라면
            min_val = min(min_val, m[j - 1] + 1) # 팰린드롬 시작 전 문자열 값 참조
    m[i] = min_val
print(m[-1])