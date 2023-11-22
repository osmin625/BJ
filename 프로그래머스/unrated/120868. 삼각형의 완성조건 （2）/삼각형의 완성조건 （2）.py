# triangle
# a + b < c

def solution(sides):
    a,b = sorted(sides)
    c_max = a + b - 1
    c_min = b - a - 1
    answer = c_max - c_min - 1
    return answer