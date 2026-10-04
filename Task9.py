
n, k = map(int, input().split())

a = []

for i in range(n):
    a.append(int(input()))

l = 0
r = 10000001

while r - l > 1:
    m = (l + r) // 2

    cnt = 0

    for length in a:
        cnt += length // m

    if cnt >= k:
        l = m
    else:
        r = m

print(l)