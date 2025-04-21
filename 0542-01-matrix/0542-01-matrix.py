class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        res = [[float('inf')] * cols for _ in range(rows)]
        queue = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    res[i][j]=0
                    queue.append((i,j))
        
        while queue:
            row,col = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if res[new_row][new_col] > res[row][col] + 1:
                        res[new_row][new_col] = res[row][col] + 1
                        queue.append((new_row, new_col))
        
        return res