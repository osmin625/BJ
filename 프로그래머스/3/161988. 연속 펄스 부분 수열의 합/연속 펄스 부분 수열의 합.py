'''
리스트 곱셈
펄스 수열 : -1과 1이 반복되는 수열. 시작은 상관 없음.
최적화 문제. dp일까 그리디일까?
bfs가 우선 떠오르지만, 수열의 길이가 최대 50만이기 때문에 시간 초과.
우선 sequence에 대해 두 가지 펄스 수열을 곱해 두고 저장하자.
이후 각 seqeunce 수열에 대해, 부분 수열의 합 중 가장 큰 것을 계산하자.
10^5
10^10 => 시간 초과.
O(n^2)이면 안됨.
그런데 길이가 정해져있지 않기 때문에 인덱스를 찾는 반복문과, 
길이를 찾는 반복문, 총 n^2으로 dp가 구현됨.
누적합 문제인가?
1 누적합과 -1 누적합의 차이가 가장 큰 지점이 최댓값.

'''
def solution(sequence):
    v = [0]
    for i,s in enumerate(sequence): v.append(v[-1] + s * [1,-1][i%2])
    return max(v) - min(v)