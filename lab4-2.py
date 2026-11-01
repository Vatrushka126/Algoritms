class Heap:
    def __init__(self, arr):
        self.heap = arr
        self.n = len(arr)

        for i in range(self.n // 2 - 1, -1, -1):
            self.sift_down(i)

    def sift_down(self, i):
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < self.n and self.heap[left] > self.heap[largest]:
                largest = left

            if right < self.n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == i:
                break

            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest

    def sort(self):
        for i in range(self.n - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.n -= 1
            self.sift_down(0)

        return self.heap


n = int(input())
arr = list(map(int, input().split()))

heap = Heap(arr)
arr = heap.sort()

print(*arr)
