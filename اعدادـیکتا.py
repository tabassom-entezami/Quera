from functools import reduce

n = int(input())

out_list = [i for i in range(n)]
out_list = list(map(int, input().split()))
for i in out_list:
    if out_list.count(i) > 1:
        out_list.remove(i)
        out_list.remove(i)


if out_list:
    res = reduce(lambda x, y: x ^ y, out_list)
    print(res)
else:
    print(0)