k = int(input())

sec = input()

list_sec = []

for i in range(k):
    list_sec.append(input())

ans = 0

for i in range(k):
    index_i = list_sec[i].index(sec[i]) + 1
    if index_i <= 5:
        ans += index_i - 1
    else:
        ans += 10 - index_i


print(ans)
