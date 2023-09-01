import sys
input = sys.stdin.readline

def is_pal(text):
    return all([t==rt for t,rt in zip(text,reversed(text))])
while True:
    n = input().rstrip()
    if not int(n):
        break
    print('yes' if is_pal(n) else 'no')