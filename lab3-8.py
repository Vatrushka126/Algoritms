from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

left = deque()
right = deque()

for i in range(n):
    s = input().split()

    if s[0] == '+':
        right.append(s[1])

    elif s[0] == '*':
        right.appendleft(s[1])

    else:
        print(left.popleft())

    if len(left) < len(right):
        left.append(right.popleft())
    elif len(left) > len(right) + 1:
        right.appendleft(left.pop())