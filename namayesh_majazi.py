k = int(input())
n = 1

for i in range(9):
    for j in range(3):
        if i == 8 and j == 0:
            print("#######################")
        elif i % 2 == 0 and i != 8:
            if j < 1 or j >= 2:
                print("########", end="")
            else:
                print(".......", end="")
        elif i != 8:
            g = False
            if j == 0 and n <= k:
                print(f"#ghorfe{n}", end="")
                n += 1
                g = True
            elif j == 2 and n <= k:
                print(f"ghorfe{n}#", end="")
                n += 1
                g = True
            elif j == 0 and g == False:
                print("#.......", end="")
            elif j == 2 and g == False:
                print(".......#", end="")
            elif j == 1:
                print(".......", end="")
    print()
