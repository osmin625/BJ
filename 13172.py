import math
M = int(input())
P = 1000000007
def dc(a,b):
    if b == 1:
        return a % P
    else:
        t = dc(a,b//2)
        if b % 2:
            return (t * t * a) % P
        else:
            return (t * t) % P
result = 0
for i in range(1,M+1):
    n,s = map(int,input().split())
    g = math.gcd(n,s)
    n //= g
    s //= g
    result += (s * dc(n,P-2)) % P
    result %= P
print(result)
