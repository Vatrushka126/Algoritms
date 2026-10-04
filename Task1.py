n, k = map(int, input().split())
data = list(map(int, input().split()))
to_search = list(map(int, input().split()))

def bin_search(data, to_search):
    left = -1
    right = len(data)
    
    while right-left > 1:
        middle = (left+right)//2
        if data[middle] < to_search:
            left = middle
        else:
            right = middle
    if right == len(data) or data[right] != to_search:
        return "NO"
    return "YES"

for i in range(k):
    print(bin_search(data, to_search[i]))
