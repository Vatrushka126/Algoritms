import heapq

n = int(input())

arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort()

heap = []

for a, b in arr:
    if heap and heap[0] <= a:
        heapq.heappop(heap)

    heapq.heappush(heap, a + b)

print(len(heap))