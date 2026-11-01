import heapq

n = int(input())
a = []

heap = []

for i in range(n):
    f = int(input())
    a.append(f)

    t = max(1000 - f, 1)
    heapq.heappush(heap, (t, i))

time = 0
pos = 0

while True:
    t, i = heapq.heappop(heap)

    if time + abs(pos - i) > t:
        print(t)
        break

    time = t
    pos = i

    a[i] += 1

    next_time = t + max(1000 - a[i], 1)
    heapq.heappush(heap, (next_time, i))
