def get_fatigue(mineral):
    out = [len(mineral), 0, 0]
    for m in mineral:
        if m == 'diamond':
            out[1] += 5
            out[2] += 25
        elif m == 'iron':
            out[1] += 1
            out[2] += 5
        else:
            out[1] += 1
            out[2] += 1
    return out

def solution(picks, minerals):
    fatigue = []
    
    if sum(picks) * 5 < len(minerals): # 8번 TC 예외 처리
        minerals = minerals[:sum(picks) * 5]
    
    for i in range(5, len(minerals) + 5, 5):
        if i >= len(minerals):
            fatigue.append(get_fatigue(minerals[i-5:len(minerals)]))
            break
        fatigue.append(get_fatigue(minerals[i-5:i]))
        
    # print(fatigue)
    fatigue.sort(key=lambda x:x[2], reverse=True)
    pidx = 0
    answer = 0
    for f in fatigue:
        while not picks[pidx]:
            pidx += 1
            if pidx == 3:
                return answer
        
        picks[pidx] -= 1
        answer += f[pidx]
            
    return answer