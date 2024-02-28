n = int(input())

place = 1
for i in range(n):
    a, b = map(int, input().split())
    if a == place:
        place = b
    elif b == place:
        place = a


print(place)
