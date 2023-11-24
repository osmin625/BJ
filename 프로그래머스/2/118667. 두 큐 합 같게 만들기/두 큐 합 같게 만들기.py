# 5:17
from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    answer = 0
    
    q1s, q2s = sum(q1), sum(q2)
    
    if (q1s + q2s) % 2:
        return -1
    
    while True:
        if answer == len(q1) * 4:
            return -1
        
        if q1s > q2s:
            value = q1.popleft()
            q2.append(value)
            q1s -= value
            q2s += value
            
        elif q2s > q1s:
            value = q2.popleft()
            q1.append(value)
            q1s += value
            q2s -= value
        
        else:
            return answer
        answer += 1
    