def isSafe(grid,r,c,oldCol):
    row = len(grid)
    col = len(grid[0])
    return (0 <= r < row) and (0 <= c < col) and grid[r][c] == oldCol


def dfs(grid,sr,sc,oldCol,newCol):
    grid[sr][sc] = newCol
    rNbr = [-1,0,0,1]
    cNbr = [0,-1,1,0]
    for i in range(4):
        if isSafe(grid,sr + rNbr[i], sc+cNbr[i],oldCol):
            dfs(grid,sr + rNbr[i], sc+cNbr[i],oldCol,newCol)
    return None

def floodFill(grid,sr,sc,oldCol,newCol):
    if oldCol == newCol:
        return grid
    dfs(grid,sr,sc,oldCol,newCol)
    return grid





image = [
    [1, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 1, 1]
]
sr, sc, newColor = 1, 2, 2

# Perform flood fill
result = floodFill(image, sr, sc, image[sr][sc], newColor)
for row in result:
    print(" ".join(map(str, row)))