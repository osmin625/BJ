# 소수의 연속합
# 자연수를 연속된 소수의 합으로 나타내기

def primes(N):
    temp = list(range(N+1))
    flag = [0 for _ in range(N+1)]

    flag[0] = 1
    flag[1] = 1
    for i in range(N+1):
        if flag[i]:
            continue
        for j in range(i+i,N+1,i):
            flag[j] = 1

    return [temp[i] for i in range(N+1) if not flag[i]]

N = int(input())
p_list = primes(N)
# print(p_list)

# max len = 283146
def cal(N):
    cnt = 0
    for len_ in range(1,283146):
        for idx in range(N+1):
            out = sum(p_list[idx:idx+len_])
            if out < N:
                continue
            elif out > N:
                if not idx:
                    return cnt
                break
            else:
                cnt += 1
                # print(out, p_list[idx:idx + len_])
                if not idx:
                    return cnt
                break
    return cnt

if N == 1:
    print(0)
else:
    print(cal(N))