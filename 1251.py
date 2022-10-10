import sys
input = sys.stdin.readline

word = input().rstrip()
word_list = []
for i in range(2,len(word)):
    for j in range(i-1):
        new = word[j::-1] + word[i-1:j:-1] + word[:i-1:-1]
        word_list.append(new)
print(sorted(word_list)[0])

