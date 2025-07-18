def isSafe(grid,r,c):
    row = len(grid)
    col = len(grid[0])
    return (0 <= r < row) and (0 <= c < col) and grid[r][c] == 'L'


def dfs(grid,r,c):
    grid[r][c] = 'W'
    rNbr = [-1,-1,-1,0,0,1,1,1]
    cNbr = [-1,0,1,-1,1,-1,0,1]
    for i in range(8):
        if isSafe(grid,r + rNbr[i], c+cNbr[i]):
            dfs(grid,r + rNbr[i], c+cNbr[i])
    return None

def countIslands(grid):
    row = len(grid)
    col = len(grid[0])
    count = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 'L':
                count = count + 1
                dfs(grid,i,j)
    return count





grid = [
    ['L', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'L'],
    ['L', 'W', 'W', 'L', 'L'],
    ['W', 'W', 'W', 'W', 'W'],
    ['L', 'W', 'L', 'L', 'W']
]
print(countIslands(grid))
print(grid)