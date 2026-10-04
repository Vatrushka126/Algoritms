n, k = map(int, input().split())

data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))


def bin_search(data, to_search):
    left = -1
    right = len(data)

    while right-left > 1:
        middle = (left+right) // 2

        if data[middle] < to_search:
            left = middle
        else:
            right = middle

    if left == -1:
        return data[right]

    if right == len(data):
        return data[left]

    if to_search - data[left] <= data[right] - to_search:
        return data[left]
    else:
        return data[right]


for i in data2:
    print(bin_search(data1, i))