'''
11:18~
과제 시작 시간이 되면 반드시 시작
하던 과제는 해당 과제를 끝내고 이어서 진행
끝낸 순서대로 기록해야 하니, 과제가 끝나는 시점을 기준으로 구현.
요약하면 stack처럼 구현
'''
from collections import deque

def timestamp(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)

def solution(plans):
    answer = []
    plans.sort(key=lambda x:x[1])
    q = deque([])
    for name, start, playtime in plans:
        start = timestamp(start)
        playtime = int(playtime)
        for _ in range(len(q)):
            end, n = q.popleft()
            if end > start:
                q.append([end + playtime, n]) # 미루기
            else:
                answer.append(n) # 정답에 추가하기
        q.appendleft([start + playtime, name])
    while q:
        end, n = q.popleft()
        answer.append(n)
    return answer