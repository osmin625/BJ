# n진수에서 소수 찾기
# 소수는 10진수 기준
# 0을 포함하지 않는 소수
def primes(N):
    temp = list(range(N+1))
    flag = [0 for _ in range(N+1)]
    flag[0], flag[1] = 1, 1
    for i in range(N+1):
        if not flag[i]:
            for j in range(i+i,N+1,i):
                flag[j] = 1
    prime_origin = [temp[i] for i in range(N+1) if not flag[i]]
    return [p for p in prime_origin if '0' not in str(p)]

def is_prime(N):    
    return all([N % i for i in range(2,int(N**0.5) + 1)])


def trans(n, k):
    out = []
    while n:
        out.append(n % k)
        n //= k
    return ''.join(map(str,list(reversed(out))))
def solution(n, k):
    out = trans(n,k)
    print(out)
    if '0' in out:
        cands = [c for c in out.split('0') if c != '']
        answer = len([c for c in list(map(int,cands)) if c in primes(1000000)])
    elif is_prime(int(out)):
        answer = 1
    else:
        answer = 0
    return answer