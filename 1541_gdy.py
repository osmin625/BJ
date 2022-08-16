import re
input = input()
numlist = re.findall('\d+',input)
callist = re.findall('\+|-',input)
temp_numlist = []
for n in numlist:
    temp_numlist.append(n.lstrip('0'))
input=''
for i in range(len(callist)+1):
    input+=temp_numlist[i]
    if i < len(callist):
        input+=callist[i]
i=0
list = input.split('-')
result = ")-(".join(list)
result = '(' + result + ')'
print(eval(result))