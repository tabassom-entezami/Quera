import string

n = int(input())
ans_each_name = []
for i in range(n):
    name = input().lower()
    ans_each_name.append(sum(1 for c in string.ascii_lowercase if name.count(c) >= 1))

print(max(ans_each_name))
