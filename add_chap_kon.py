n = (input())
s = len(n)
n = int(n)
for i in range(s - 1, -1, -1):
    dah = 10 ** i
    a = int(n / dah)
    n = int(n % dah)
    if (a == 0):
        print("0:")
    else:
        ans = 0
        for j in range(0, (a)):
            ans = (ans * 10) + 1
        ans = ans * a
        an = str(a) + ":"
        print(an, ans)
