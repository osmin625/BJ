import string

def solution(msg):
    # 사전 초기화
    dict_ = {c:i+1 for i,c in enumerate(string.ascii_uppercase)}
    max_len = 1
    max_idx = 26
    answer = []
    i = 0
    def find_str(i):
        nonlocal dict_, msg, max_len
        for l in range(max_len, 0, -1):
            if msg[i:i+l] in dict_:
                return msg[i:i+l]
    while i < len(msg):
        out = find_str(i) # 사전에서 가장 긴 일치하는 문자열 찾기
        answer.append(dict_[out]) # 색인 번호 출력
        max_idx += 1
        next_ = msg[i:i+len(out) + 1]
        dict_[next_] = max_idx
        max_len = max(len(next_), max_len)
        i += len(out)
        
    print(answer)
    return answer