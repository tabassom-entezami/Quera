n, real = input().split()

for i in range(int(n)):
    uses = []
    code = input()
    for j in code:
        if j not in real:
            print('No')
            break
        uses.append(j)
    else:
        for j in real:
            if j not in uses:
                print('No')
                break
        else:
            print('Yes')


