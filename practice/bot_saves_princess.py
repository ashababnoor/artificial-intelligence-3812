# Problem taken from HackerRank -> https://www.hackerrank.com/challenges/saveprincess

#!/usr/bin/python

'''
SAMPLE INPUT
------------
3
---
-m-
p--

SAMPLE OUTPUT
-------------
DOWN
LEFT

'''

def displayPathtoPrincess(n,grid):
#print all the moves here
    mPos = [0, 0]
    pPos = [0, 0]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'm':
                mPos = [i, j]
            if grid[i][j] == 'p':
                pPos = [i, j]
    
    # print('pPos is:', pPos, pPos[0], pPos[1])
    # print('mPos is:', mPos, mPos[0], mPos[1])
    
    xDist = pPos[1] - mPos[1]
    yDist = pPos[0] - mPos[0]
    
    # print('xDist is:', xDist)
    # print('yDist is:', yDist)

    if yDist < 0:
        for i in range(abs(yDist)):
            print('UP')
    else:
        for i in range(yDist):
            print('DOWN')
    if xDist < 0:
        for i in range(abs(xDist)):
            print('LEFT')
    else:
        for i in range(xDist):
            print('RIGHT')
    
    
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)