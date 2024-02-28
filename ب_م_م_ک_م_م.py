n, m = map(int, input().split())


def bmm(a, b):
    if (b == 0):
        return a
    else:
        return bmm(b, a % b)


ans1 = bmm(n, m)
ans2 = (m * n) / ans1

print(ans1, int(ans2))
