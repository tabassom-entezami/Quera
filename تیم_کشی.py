a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
a3 = int(input())
b3 = int(input())
ans = 0
if a1 - b1 > 0:
    ans += b1
else:
    ans += a1

if a2 - b2 > 0:
    ans += b2
else:
    ans += a2

if a3 - b3 > 0:
    ans += b3
else:
    ans += a3

print(ans)