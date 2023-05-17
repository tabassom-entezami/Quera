n, m = map(int, input().split())
costs = [list(map(int, input().split())) for i in range(n)]
travels = [list(map(int, input().split())) for i in range(m)]
out_go = 0

for travel in travels:
    out_go += costs[travel[0]-1][travel[1]-1]

print(out_go)
