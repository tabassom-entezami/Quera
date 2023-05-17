n, x, k = map(int, input().split())

kanal = []
for i in range(n):
    kanal.append(input())

now = (k+x) % n
print(kanal[now - 1])
