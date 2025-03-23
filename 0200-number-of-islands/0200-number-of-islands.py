class Solution:
    def isValid(self,i,j,visited,grid):
        row = len(grid)
        col = len(grid[0])
        return 0<=i<row and 0<=j<col and visited[i][j]!=1 and grid[i][j]=='1'
    
    def DFS(self,i,j,visited,grid):
        visited[i][j] = 1
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for dir in directions:
            newRow = i+dir[0]
            newCol = j+dir[1]
            if self.isValid(newRow,newCol,visited,grid):
                self.DFS(newRow,newCol,visited,grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:  # Added empty grid check
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        count =0

        for i in range(rows):
            for j in range(cols):
                if visited[i][j]!=1 and grid[i][j]== '1':
                    count+=1
                    self.DFS(i,j,visited,grid)
        return count

  