def solution(bandage, health, attacks):    
    # 
    # bandage = [t, x, y]
    # t초동안 초당 x씩 회복
    # t초 연속 성공시 y만큼 추가로 회복.
    # 최종 t* x + y만큼 회복
    # 공격 당하면 연속 시간 0초로 초기화
    # 피격시 체력 - 피해량
    t, x, y = bandage
    h = health
    prev = 0
    for time, dam in attacks:
        h += (time - prev - 1) * x
        if time - prev > t:
            h += y * ((time - prev - 1) // t)
        h = min(health, h)
        h -= dam
        if h <= 0:
            break
        prev = time
    return h if h > 0 else -1