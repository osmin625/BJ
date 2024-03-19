from itertools import combinations, product
from collections import Counter
# 6면 주사위 n개
# 주사위에 적힌 숫자는 모두 다름
# A가 먼저 가져감
# A가 가져간 주사위들의 합계가 B가 가져간 주사위들의 합계보다 커야 함.
# n = 10인 경우 (최대 경우의 수)
# 10C5 = 9 * 4 * 7 = 252
# 252 * 36 * 36 < 10,000,000
# 구현 문제
# 주사위 2개 고르기
# 2개 주사위 합계 산출하기
# 승무패 결과 세기

def solution(dice):
    # 주사위 n개 조합
    def choose_(dice):
        dice_idx = list(range(1, len(dice) + 1))
        selected = list(combinations(dice_idx,len(dice)//2))
        ls = len(selected) // 2
        return selected[:ls], list(reversed(selected[ls:]))

    def sum_dices(d):
        # input: 주사위 여러 개의 인덱스
        # output: 가능한 합계
        return Counter(map(sum,product(*[dice[i-1] for i in d])))
    
    
    def compare_dices_sum(d1, d2):
        win, draw, loss = 0, 0, 0
        result1, result2 = sum_dices(d1), sum_dices(d2)
        for r1, r2 in product(result1, result2):
            cases = result1[r1] * result2[r2]
            if r1 > r2:
                win += cases
            elif r1 < r2:
                loss += cases
            else:
                draw += cases
        print(win, draw, loss)
        return [win, draw, loss]
        
    result = []
    slct_dices, unslct_dices = choose_(dice)
    for slct, unslct in zip(slct_dices, unslct_dices):
        result.append([compare_dices_sum(slct, unslct),slct, unslct])
    result.sort(key=lambda x:max(x[0][0],x[0][2]), reverse=True)
    temp = result[0]
    answer = temp[1] if temp[0][0] > temp[0][2] else temp[2]
    return answer