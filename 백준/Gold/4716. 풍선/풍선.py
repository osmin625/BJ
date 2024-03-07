def solution():
    global A, B
    ans = 0
    for k, a_dist, b_dist in teams:
        if a_dist > b_dist:
            if B >= k:
                B -= k
                ans += k * b_dist
            else:
                k -= B
                ans += B * b_dist
                B = 0
                A -= k
                ans += k * a_dist
        else:
            if A >= k:
                A -= k
                ans += k * a_dist
            else:
                k -= A
                ans += A * a_dist
                A = 0
                B -= k
                ans += k * b_dist
    return ans


while True:
    N,A,B = map(int,input().split())
    if not N:
        break
    else:
        teams = [list(map(int,input().split())) for i in range(N)]
        ans = 0
        # distance gap 큰 것 우선
        teams.sort(key=lambda x: [abs(x[1] - x[2]),x[1]+ x[2]], reverse=True)
        print(solution())
