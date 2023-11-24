def failure_rate(stages,n):
    reach = len([s for s in stages if s >= n])
    if not reach:
        return 0
    fail = stages.count(n)
    return fail / reach
def solution(N, stages):
    rate = [[i, 0] for i in range(1,N+1)]
    for i in range(N):
        rate[i][1] = failure_rate(stages,i+1)
    rate.sort(key=lambda x:x[1], reverse=True)
    print(rate)
    answer = [r[0] for r in rate]
    return answer