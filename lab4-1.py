class Heap:
    def __init__(self):
        self.heap = []

    def Insert(self, k):
        self.heap.append(k)
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent] >= self.heap[i]:
                break

            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def Extract(self):
        result = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        i = 0
        n = len(self.heap)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left

            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == i:
                break

            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest

        return result


n = int(input())
heap = Heap()

for i in range(n):
    command = input().split()

    if command[0] == '0':
        heap.Insert(int(command[1]))
    else:
        print(heap.Extract())
