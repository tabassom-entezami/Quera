a ,b = map(int,input().split())

a = abs(12 - a)
b = abs(60 - b)
if b is 60 :
    b = 0
if a is 12:
    a = 0

print('%.2d:' % a ,end='')
print('%.2d' % b)