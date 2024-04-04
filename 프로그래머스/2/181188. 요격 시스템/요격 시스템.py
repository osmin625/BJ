from heapq import heapify, heappop
'''
A나라가 B나라에 융단 폭격
폭격 요격해야 함.
2차원 공간
A는 x축으로 미사일 발사. (s, e)
B나라는 y축으로 요격 미사일 발사
x좌표에 걸친 모든 미사일 요격.
s, e는 제외.
요격 미사일은 실수 좌표에서도 발사 가능.

idea
미사일을 s 좌표 순으로 정렬.
요격되지 않은 미사일의 e 좌표에 도달하면 요격.

'''

def solution(targets):
    targets.sort()
    intercept = 0
    answer = 0
    for s, e in targets:
        if s >= intercept:
            answer += 1
            intercept = e
        if e < intercept:
            intercept = e
    return answer