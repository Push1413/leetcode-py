class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        isVisited = [[0 for _ in range(cols)]for _ in range(rows)]
        perimeter = 0
        store = {}

        def DFS(i,j):
            counter =0
            isVisited[i][j]=1
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for dir in directions:
                newRow = dir[0]+i
                newCol = dir[1]+j

                if isCheck(newRow,newCol):
                    counter+=1
            
            return counter

        def isCheck(newRow,newCol):
            return 0<=newRow<rows and 0<=newCol<cols and grid[newRow][newCol]==1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and isVisited[i][j]==0:
                    count = DFS(i,j)
                    store[(i,j)]=count
        
        for value in store.values():
            if value==3:
                perimeter+=1
            elif value == 2:
                perimeter+=2
            elif value==1:
                perimeter+=3
            elif value==0:
                perimeter+=4
        return perimeter
        
       