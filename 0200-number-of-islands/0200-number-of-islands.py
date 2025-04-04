class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)]for _ in range(rows)]
        count =0

        def isSafe(newRow,newCol):
            return 0<=newRow<rows and 0<=newCol<cols and grid[newRow][newCol]=="1" and visited[newRow][newCol]==0

        def DFS(row,col):
            visited[row][col] = 1
            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            for rx,cy in directions:
                newRow = row + rx
                newCol = col + cy

                if isSafe(newRow, newCol):
                    DFS(newRow,newCol)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    count+=1
                    DFS(i,j)
        
        return count