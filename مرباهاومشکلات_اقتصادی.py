import math

n, k = map(int, input().split())
jars_sum = sum(map(int, input().split()))

print(n - math.ceil(jars_sum/k))
