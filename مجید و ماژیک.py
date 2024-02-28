from collections import defaultdict

n = int(input())
array = defaultdict(lambda: 0)
a = list(map(int, input().split()))
for v in a:
    array[v] += 1


m = 0
min_index = 1
for i in range(100):
    if array[i] != 0:
        m = array[i]
        min_index = i
        break

for i in range(100):
    if array[i] < m and array[i] != 0:
        m = array[i]
        min_index = i

print(min_index)
