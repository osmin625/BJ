# 10:30 ~ 
# 09:00부터 n회, t분 간격, m명 승객 탑승 가능
# 09:00에 줄 선 승객 탑승 가능
# 사무실 갈 수 있는 도착 시간 중 제일 늦은 시각
# 같은 시각 도착한 크루중 제일 뒤.
# 버스 탑승 시간만 구하면 됨.
def solution(n, t, m, timetable):
    answer = 0
    # 시간 숫자로 변환하기
    def t2m(time):
        h, m = map(int,time.split(':'))
        return h * 60 + m
    # 숫자 시간으로 변환하기
    def m2t(minute):
        return str(minute // 60).rjust(2,'0') + ':' + str(minute % 60).rjust(2,'0')
    # 마지막 버스의 시간 구하기.
    def last_bus_time():
        nonlocal n, t
        return m2t(t2m("09:00") + t * (n-1))
    # 마지막 버스까지 남은 사람 구하기
    def remain_person(n, t, m, timetable):
        persons = sorted(list(map(t2m,timetable)),reverse=True)
        bus = 540
        while n != 1 and persons:
            for i in range(m):
                if not persons:
                    break
                elif persons[-1] <= bus:
                    persons.pop()
            bus += t
            n-= 1
        return persons
    
    rp = remain_person(n,t,m,timetable)
    if m > len(rp):
        return last_bus_time()
    else:
        return m2t(min([t2m(last_bus_time()),rp[-m] - 1]))
        
        
