'''
초침과 시침이 겹칠 때 알람
초침과 분침이 겹칠 때 알람
시간 범위 내에서 알람이 울린 횟수 계산하기
구현 문제
최대 24시간.
구현
시침의 위치
분침의 위치
초침의 위치
time2sec
sec2time

# 반례 구현 실패.
# 참조: https://school.programmers.co.kr/questions/63464
'''
'''
def time2sec(h, m, s):
    return h * 60 ** 2 + m * 60 + s

def sec2time(sec):
    h = sec // 60 ** 2
    m = sec % 60 ** 2 // 60
    s = sec % 60
    return h, m, s

def locate_pin_(h, m, s):
    # 시침
    hT = CT / 12
    hmT = hT / 60
    hsT = hmT / 60
    
    # 분침
    mT = CT / 60
    msT = mT / 60
    
    # 초침
    sT = CT / 60
    
    # 시침, 분침, 초침 위치
    return round(hT * (h % 12) + hmT * m + hsT * s, 3),\
            round(mT * m + msT * s, 3), \
            round(sT * s, 3) 

def hour_pin_overlap(bh, bm, bs, hp, mp, sp): # 1초전 바늘과 현재 바늘 위치 비교
    # 바늘이 360도(12시)를 지날 때 부호가 역전되는 반례 발생. -> 해결
    # 1초 안에 두 번 겹칠 때 반례 발생 -> 구현 실패.
    if hp < bh:
        hp += 360
    if sp < bs:
        sp += 360
    return (bh - bs) * (hp - sp) <= 0

def minute_pin_overlap(bh, bm, bs, hp, mp, sp):
    if mp < bm:
        mp += 360
    if sp < bs:
        sp += 360
    return (bm - bs) * (mp - sp) <= 0
def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    bh, bm, bs = locate_pin_(h1, m1, s1)
    for sec in range(time2sec(h1, m1, s1) + 1, time2sec(h2, m2, s2) + 1):
        hp, mp, sp = locate_pin_(*sec2time(sec))
        if hour_pin_overlap(bh, bm, bs, hp, mp, sp):
            # print(sec2time(sec), (bh - bs) * (hp - sp) <= 0, (bm - bs) * (mp - sp) <= 0)
            answer += 1
        if minute_pin_overlap(bh, bm, bs, hp, mp, sp):
            answer += 1
        
        bh, bm, bs = hp, mp, sp
    return answer
'''

CT = 360 # Clock_Theta
def locate_pin_(h, m, s):
    # 시침
    hT = CT / 12
    hmT = hT / 60
    hsT = hmT / 60
    
    # 분침
    mT = CT / 60
    msT = mT / 60
    
    # 초침
    sT = CT / 60
    
    # 시침, 분침, 초침 위치
    return hT * (h % 12) + hmT * m + hsT * s, mT * m + msT * s, sT * s

def get_cnt(h, m, s):
    cnt = -1
    cnt += (h * 60 + m) * 2
    cnt -= h
    if h >= 12:
        cnt -= 2
    hPin, mPin, sPin = locate_pin_(h, m, s)
    cnt += hPin <= sPin
    cnt += mPin <= sPin
    return cnt
def solution(h1, m1, s1, h2, m2, s2):
    answer = get_cnt(h2, m2, s2) - get_cnt(h1,m1,s1)
    if h1 in [0, 12] and not m1 and not s1:
        answer += 1
    return answer