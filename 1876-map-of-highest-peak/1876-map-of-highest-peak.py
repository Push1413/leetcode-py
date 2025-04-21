class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        cols = len(isWater[0])
        res = [[-1 for _ in range(cols)]for _ in range(rows)]
        queue = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    res[i][j]=0
                    queue.append((i,j))
        
        while queue:
            x,y = queue.popleft()
            for dx, dy in directions:
                newRow = dx+x
                newCol = dy+y

                if 0<=newRow<rows and 0<=newCol<cols and res[newRow][newCol]==-1:
                    res[newRow][newCol] = res[x][y] + 1
                    queue.append((newRow,newCol))

        return res
        