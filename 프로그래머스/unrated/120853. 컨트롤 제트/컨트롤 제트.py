def solution(s):
    nums = s.split()
    temp = [int(nums[i]) for i in range(len(nums)-1) if nums[i+1] != 'Z' and nums[i] != 'Z']
    if nums[-1] != 'Z':
        temp.append(int(nums[-1]))
    print(temp)
    answer = sum(temp)
    
    return answer