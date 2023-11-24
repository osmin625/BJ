import string
def parser(str_):
    temp = [''.join([str_[i],str_[i+1]]) for i in range(len(str_)-1)]
    out = [t.lower() for t in temp if t[0] in string.ascii_letters and t[1] in string.ascii_letters]
    return out
def solution(str1, str2):
    s1 = parser(str1)
    # print(s1)
    s2 = parser(str2)
    # print(s2)
    if s1 == s2:
        return 65536
    its = []
    uni = s2.copy()
    while s1:
        s = s1.pop()
        if s in s2:
            its.append(s)
            s2.remove(s)
        uni.append(s)
    
    answer = len(its) / (len(uni)-len(its)) * 65536
    return int(answer)