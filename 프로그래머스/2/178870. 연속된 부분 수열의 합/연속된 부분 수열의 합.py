'''
투포인터
뒤에서부터 접근
'''
def solution(sequence, k):
    sum_ = 0
    end = len(sequence) - 1
    for start in range(len(sequence) - 1, -1, -1):
        sum_ += sequence[start]
        # print(sum_, start, end)
        if sum_ < k:
            continue
        elif sum_ > k: # 합이 k보다 큰 경우
            sum_ -= sequence[end] # 다시 뺌
            end -= 1
        else: # 합이 k인 경우 -> 최소 인덱스 찾기
            while sequence[start - 1] == sequence[end] and start>0:
                start-=1
                end -= 1
            return [start, end]
    answer = []
    return answer