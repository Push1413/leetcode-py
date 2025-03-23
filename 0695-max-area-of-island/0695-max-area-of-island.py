class Solution:
    def isValid(self,i,j,visited,grid):
        rows = len(grid)
        cols = len(grid[0])
        return 0<=i<rows and 0<=j<cols and grid[i][j]==1 and visited[i][j]==0
    
    def DFS(self,i,j,visited,grid,count):
        count1 = count
        visited[i][j] = 1
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for dir in directions:
            newRow = i + dir[0]
            newCol = j + dir[1]
            if self.isValid(newRow,newCol,visited,grid):
                count1 +=1
                count1 = self.DFS(newRow,newCol,visited,grid,count1)
        return count1

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        maxArea = 0

        for i in range(rows):
            for j in range(cols):
                if visited[i][j]==0 and grid[i][j]==1:
                    area = self.DFS(i,j,visited,grid,1)
                    maxArea = max(maxArea,area)

        return maxArea

    

                

        