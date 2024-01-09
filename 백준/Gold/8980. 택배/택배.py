import sys
input = sys.stdin.readline
N, C = map(int, input().split())  # 마을 수, 트럭 용량
M = int(input())  # 박스 정보 개수
arr = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: x[1])
truck = [0] * N
ans = 0
for start, end, box in arr:
    max_box = box # 처음엔 목표치 전부 다 보내는걸로 간주.
    # 얼마나 보낼 수 있는지 계산
    for i in range(start, end): # 중간 마을에서 보낼 박스가 있어 공간이 부족하면
        max_box = min(max_box, C - truck[i]) # 남는 만큼만 보냄.
    # 다음 공간 계산을 위해 이동 중인 박스 기록하기
    for i in range(start, end):
        truck[i] += max_box
    ans += max_box
print(ans)