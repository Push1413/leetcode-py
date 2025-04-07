class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        atlanta = [[0 for _ in range(cols)]for _ in range(rows)]
        pacific = [[0 for _ in range(cols)]for _ in range(rows)]
        output = []

        def DFS(i,j,visited, prev):
            if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j] or heights[i][j]< prev:
                return 
            visited[i][j] = 1
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dr, dc in directions:
                DFS(i + dr, j + dc, visited, heights[i][j])     

        for i in range(rows):
            DFS(i,0,pacific,heights[i][0])
            DFS(i,cols-1,atlanta,heights[i][cols-1])

        for j in range(cols):
            DFS(0,j,pacific,heights[0][j])   
            DFS(rows-1,j,atlanta,heights[rows-1][j])  

        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] and atlanta[i][j]:
                    output.append([i, j])
        
        return output


        