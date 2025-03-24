from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        q = deque()
        fresh_oranges = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                elif grid[i][j]==1:
                    fresh_oranges +=1
        
        directions = [(1,0),(0,-1),(0,1),(-1,0)]
        minutes = 0
        
        while q:
            dx, dy, time = q.popleft()
            minutes = max(minutes, time)

            for dir in directions:
                newRow = dx+dir[0]
                newCol = dy+dir[1]

                if 0<=newRow<row and 0<=newCol<col and grid[newRow][newCol]==1:
                    grid[newRow][newCol]=2
                    q.append((newRow,newCol,time+1))
                    fresh_oranges -=1
        
        if fresh_oranges == 0:
            return minutes
        else:
            return -1

                    





        