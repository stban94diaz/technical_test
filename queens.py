import random

'''
    [0, 0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 0, 0, 0]

      0  1  2  3  4  5  6  7
    0[x, 0, 0, 0, 0, 0, 0, 0]
    1[0, 0, 0, x, 0, 0, 0, 0]
    2[0, 0, 0, 0, 0, 0, 0, 0]
    3[0, 0, 0, 0, x, 0, 0, 0]
    4[0, 0, 0, 0, 0, 0, 0, 0]
    5[0, 0, 0, 0, 0, 0, 0, 0]
    6[0, 0, 0, 0, 0, 0, 0, 0]
    7[0, 0, 0, 0, 0, 0, 0, 0]
'''

n = 8

pos = []
while len(pos)<n:
    pos = []
    m = [['0' for i in range(n)] for i in range(n)]

    f = random.randint(0, n-1)
    c = random.randint(0, n-1)
    while((f==0 and c==0) or
          (f==0 and c==n-1) or
          (f==n-1 and c==0) or
          (f==n-1 and c==n-1)):
        f = random.randint(0, n-1)
        c = random.randint(0, n-1)

    m[f][c] = 'x'
    pos.append((f, c))

    for i in range(n):
        for j in range(0,n):
            if((i==0 and j==0) or
              (i==0 and j==n-1) or
              (i==n-1 and j==0) or
              (i==n-1 and j==n-1)):
                  continue
            b = False
            for e in pos:
                if(e[0] == i or e[1] == j or
                   ((max(i, e[0])-min(i, e[0])) ==
                   (max(j, e[1])-min(j, e[1])))):
                    b = True
            if b == False:
                m[i][j] = 'x'
                pos.append((i, j))

print(pos)
for row in m:
    print(row)
