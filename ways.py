#!/bin/python3

import sys

def getWays(n, c):
    c.sort()
    if n == 0:
        print 0
    else:
        print( _get_ways(n, c[::-1]) )

def _get_ways(n, c, curren_way=0, res=0, level=0, _buffer={}):
    print(_buffer)
    if curren_way == n:
        return res + 1
    elif curren_way > n:
        return res

    for v in c:
        curren_way += v
        if curren_way <= n:
            _res = res
            if not (str(curren_way-v)+'-'+str(v) in _buffer):
                res = _get_ways(n, c, curren_way, res, level+1, _buffer)
                _buffer[str(curren_way-v)+'-'+str(v)] = res-_res
            else:
                res += _buffer[str(curren_way-v)+'-'+str(v)]
        c = c[1:]
        curren_way -= v

    return res

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
