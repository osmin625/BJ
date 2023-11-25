# 점수 0~10
# 영역 s, d, t => 점수 1, 2, 3제곱
# 옵션 스타, 아차 => 직전, 현재 2배 or -현재
# 스타, 아차 스스로, 서로 중첩 가능(4배 or -2배)
# s, d, t 점수마다 하나
# 스타, 아차 최대 둘 중 하나

def solution(dartResult):
    dr = dartResult
    answer = 0
    area = {'S':1, 'D':2, 'T':3}
    i = 0
    prev_score = 0
    score = 0
    while i < len(dr):
        print(score)
        if dr[i+1].isdigit():
            score = int(dr[i:i+2]) ** area[dr[i+2]]
            i += 1
        else:
            score = int(dr[i]) ** area[dr[i+1]]
        if i + 2 < len(dr):
            if dr[i+2].isdigit():
                i += 2
                answer += prev_score
                prev_score = score
                continue
            elif dr[i+2] == '*':
                prev_score *= 2
                score *= 2
            else:
                score *= -1
            i += 3
        else:
            i += 2
        answer += prev_score
        prev_score = score
    answer += score
    
    return answer