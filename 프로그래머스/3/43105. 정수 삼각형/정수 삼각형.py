def solution(triangle):
    answer = 0
    for i in range(1,len(triangle)):
        triangle[i][0] += triangle[i-1][0]
        triangle[i][-1] += triangle[i-1][-1]
        for j in range(1,i):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
            # print(triangle[i][j])
    answer = max(triangle[i])
    return answer