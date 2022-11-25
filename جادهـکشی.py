n = int(input())

if n % 2 == 0:
    print(int(((n / 2) + 1) * ((n / 2) + 1)))
else:
    print(int((int(n / 2) + 1) * ((int(n / 2) + 1)+1)))
