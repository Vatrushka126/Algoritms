n = int(input())
a = list(map(int, input().split()))

stack = []
next_wagon = 1

for i in range(n):
    stack.append(a[i])

    while len(stack) > 0 and stack[-1] == next_wagon:
        stack.pop()
        next_wagon += 1

if next_wagon == n + 1:
    print("YES")
else:
    print("NO")