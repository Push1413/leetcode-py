class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        count = 0

        def isValid(newRow,newCol):
            return 0<=newRow<rows and 0<=newCol<cols and visited[newRow][newCol]==0 and grid[newRow][newCol]=='1'


        def DFS(row,col):
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            visited[row][col]=1

            for dx,dy in directions:
                newRow = dx + row
                newCol = dy + col

                if isValid(newRow,newCol):
                    DFS(newRow,newCol)



        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1' and visited[i][j]==0:
                    count+=1
                    DFS(i,j)
        return count

        