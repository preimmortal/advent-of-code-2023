from collections import deque

matrix = []
f = open("./input", "r")
for line in f.readlines():
    matrix.append([])
    for c in line.rstrip("\n"):
        matrix[-1].append(c)

n = len(matrix)
m = len(matrix[0])
numbers = { '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' }

# For each * in the matrix, identify all adjacent numbers to it
#   Find the start of each of those numbers
#   If there are exactly two start positions, then multiply the two numbers
#   Add to res
def findStartOfNumber(i,j):
    while j-1 >= 0 and matrix[i][j-1] in numbers:
        j -= 1
    return i,j

def findNumber(i,j):
    num = 0
    startI, startJ = findStartOfNumber(i,j)
    i, j = startI, startJ
    while j < m and matrix[i][j] in numbers:
        num = num*10 + int(matrix[i][j])
        j += 1
    return (num,startI,startJ)

def bfs(r,c):
    adj = [(r-1,c-1), (r-1,c), (r-1,c+1), 
           (r,c-1), (r,c+1), 
           (r+1,c-1), (r+1,c), (r+1,c+1)]

    numbersList = {}

    for nr,nc in adj:
        if (nr >= 0 and nr < n and nc >= 0 and nc < m
            and matrix[nr][nc] in numbers):
            num,i,j = findNumber(nr,nc)
            numbersList[(i,j)] = num
    res = 1
    if len(numbersList.keys()) == 2:
        for key in numbersList:
            res *= numbersList[key]
        return res
    return 0

total = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == '*':
            total += bfs(i,j)

print(total)

