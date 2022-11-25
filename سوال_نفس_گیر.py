n = int(input())
ais = list(map(int, input().split()))
bis = list(map(int, input().split()))

print( sum([(int(ais[i]) * int(bis[i])) for i in range(n)]))
