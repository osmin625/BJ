A, B, C = map(int, input().split())
def dc(A,B):
    if B == 1:
        return A % C
    else:
        t = dc(A,B//2)
        if B % 2:
            return (t * t * A) % C
        else:
            return (t * t) % C
print(dc(A,B))
