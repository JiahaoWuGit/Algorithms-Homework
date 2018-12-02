# -*- coding:UTF-8 -*-
a = list('ABCBDAB')
b = list('BDCABA')

a = [0] + a
b = [0] + b
lena = len(a)
lenb = len(b)
num = [[0 for col in range(lena)] for row in range(lenb)]
direction = [[0 for col in range(lena)] for row in range(lenb)]
result = []

for i in range(1,lenb):
    for j in range(1,lena):
        if a[j] > b[i]:
            num[i][j] = num[i-1][j]
            direction[i][j] = 'up'
        elif a[j] == b[i]:
            num[i][j] = num[i-1][j-1] + 1
            direction[i][j] = 'dia'
        else:
            num[i][j] = num[i][j-1]
            direction[i][j] = 'left'
    print num[i]
    print direction[i]
y = lena - 1
x = lenb - 1
#print x,y
while 1:

    print a[y],direction[x][y]
    if direction[x][y] == 'up':
        x =x-1
    elif direction[x][y] == 'left':
        y= y-1
    elif direction[x][y] == 'dia':
        result.append(a[y])
        x = x-1
        y = y-1
    if direction[x][y] == 0:
        break

print 'The longest common string is :'
print result
print 'the length of it is: ',num[lenb-1][lena-1]
