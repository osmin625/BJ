K = int(input())
size_ = 1
while K > size_:
    size_ *= 2
print(size_, end=' ')
cnt = 0
while K:
    if K >= size_:
        K -= size_
    if not K:
        break
    cnt += 1
    size_ //= 2
print(cnt)