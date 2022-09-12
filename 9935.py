string = input()  # 전체 문자열
bomb = input()  # 폭발 문자열

stack = []
bl = len(bomb)
for char in string:
    stack.append(char)
    if char == bomb[-1] and ''.join(stack[-bl:]) == bomb:
        del stack[-bl:]
answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)

