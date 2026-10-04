from math import sqrt

c = float(input())

def bin_search(c):
    left = 0
    right = c

    for i in range(100):
        middle = (left + right) / 2

        if middle ** 2 + sqrt(middle) < c:
            left = middle
        else:
            right = middle

    return middle

print(bin_search(c))
