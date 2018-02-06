#!/bin/python3

import sys

def getWays(n, c):
    res = [0 for i in range(n+1)]
    res[0] = 1
    for coin in c:
        for i in range(1, n+1):
            if (i - coin) >= 0:
                res[i] += res[i - coin]
    print( res[n] )

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
