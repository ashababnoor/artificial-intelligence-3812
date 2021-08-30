# Problem taken from HackerRank -> https://www.hackerrank.com/challenges/saveprincess2

#!/usr/bin/python

'''
SAMPLE INPUT
------------
5
2 3
-----
-----
p--m-
-----
-----

SAMPLE OUTPUT
-------------
LEFT

'''

def nextMove(n,r,c,grid):
    mPos = [r, c]
    pPos = [0, 0]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                pPos = [i, j]
                break
        else:
            continue
        break

    # print('pPos is:', pPos, pPos[0], pPos[1])
    # print('mPos is:', mPos, mPos[0], mPos[1])
    
    xDist = pPos[1] - mPos[1]
    yDist = pPos[0] - mPos[0]
    
    # print('xDist is:', xDist)
    # print('yDist is:', yDist)

    if yDist == 0:
        if xDist < 0:
            return 'LEFT'
        elif xDist > 0:
            return 'RIGHT'
    elif xDist == 0:
        if yDist < 0:
            return 'UP'
        elif yDist > 0:
            return 'DOWN'
    else:
        if yDist < 0:
            return 'UP'
        elif yDist > 0:
            return 'DOWN'
    return ''

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))