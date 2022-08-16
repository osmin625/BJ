num_list = [1,1,1,2,2,3,4,5,7,9]
case_count = input()
for i in range(10,100):
    num_list.append(num_list[i-1] + num_list[i-5])
def p(n):
    print(num_list[n-1])
for i in range(1,int(case_count)+1):
    p(int(input()))