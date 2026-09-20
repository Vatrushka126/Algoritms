distance = list(map(int, input().split()))
tariff = list(map(int, input().split()))

distance.sort()
tariff.sort(reverse=True)

sum = 0

for i in range(len(distance)):
    sum += distance[i] * tariff[i]

print(sum)