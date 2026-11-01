import heapq

n = int(input())
arr = list(map(int, input().split()))

heapq.heapify(arr)

s = 0

while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)

    c = a + b
    s += c * 0.05

    heapq.heappush(arr, c)

print(f"{s:.2f}")
