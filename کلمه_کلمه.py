name = input()


sounds = ['a', 'o', 'e', 'i', 'u']
more = 0
for i in name:
    if i in sounds:
        more+=1

print(2**more)
