# BFS on all symbols and mark all non-dot characters true
# Do a second pass to find all numbers were marked true by the BFS
from collections import deque

matrix = []
f = open("./input", "r")
for line in f.readlines():
    matrix.append([])
    for c in line.rstrip("\n"):
        matrix[-1].append(c)

symbols = {'~', ':', "'", '+', '[', '\\', '@', '^', 
            '{', '%', '(', '-', '"', '*', '|', ',', 
            '&', '<', '`', '}', '_', '=', ']', '!', 
            '>', ';', '?', '#', '$', ')', '/'}
numbers = { '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' }


# BFS
n = len(matrix)
m = len(matrix[0])
visited = set()
validPartPositions = [[False for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

def bfs(i,j):

    q = deque()
    q.append((i,j))
    while q:
        r,c = q.popleft()
        validPartPositions[r][c] = True
        adj = [(r-1,c-1), (r-1,c), (r-1,c+1), 
               (r,c-1), (r,c+1), 
               (r+1,c-1), (r+1,c), (r+1,c+1)]
        for nr,nc in adj:
            if (nr >= 0 and nr < n and nc >= 0 and nc < m
               and (nr,nc) not in visited 
               and matrix[nr][nc] in numbers):
                q.append((nr,nc))
                visited.add((nr,nc))

for i in range(n):
    for j in range(m):
        if (i,j) in visited or matrix[i][j] in numbers or matrix[i][j] == '.':
            continue
        visited.add((i,j))
        bfs(i,j)

# Go through all valid part positions and sum up their numbers
res = 0
for i in range(n):
    currentNumber = 0
    for j in range(m):
        if matrix[i][j] in numbers and validPartPositions[i][j]:
            currentNumber = currentNumber*10 + int(matrix[i][j])
        else:
            res += currentNumber
            currentNumber = 0
    res += currentNumber

print(res)

