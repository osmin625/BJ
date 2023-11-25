def num_conv_alpha(n):
    if n >= 10:
        return chr(ord('A') + n - 10)
    return str(n)

def cal_jin(n, num):
    out = ['0']
    for i in range(num):
        iout = []
        while i:
            iout.append(num_conv_alpha(i % n))
            i //= n
        out.extend(iout[::-1])
    return out

def solution(n, t, m, p):
    all_num = cal_jin(n,t * m)
    answer = [all_num[i] for i in range(p-1,m * t,m)]
    return ''.join(answer)