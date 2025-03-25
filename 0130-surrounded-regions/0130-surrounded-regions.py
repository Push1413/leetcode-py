class Solution:
    def isValid(self, i, j, board, visited):
        rows = len(board)
        cols = len(board[0])
        return 0 <= i < rows and 0 <= j < cols and visited[i][j] == 0 and board[i][j] == "O"

    def DFS(self, i, j, board, visited):
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        stack = [(i, j)]
        visited[i][j] = 1

        while stack:
            x, y = stack.pop()
            for dx, dy in directions:
                newX, newY = x + dx, y + dy
                if self.isValid(newX, newY, board, visited):
                    visited[newX][newY] = 1
                    stack.append((newX, newY))



    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        rows = len(board)
        cols = len(board[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
      

        for i in range(rows):
            if board[i][0] == "O" and not visited[i][0]:  # Left border
                self.DFS(i, 0, board, visited)
            if board[i][cols - 1] == "O" and not visited[i][cols - 1]:  # Right border
                self.DFS(i, cols - 1, board, visited)
        
        for j in range(cols):
            if board[0][j] == "O" and not visited[0][j]:  # Top border
                self.DFS(0, j, board, visited)
            if board[rows - 1][j] == "O" and not visited[rows - 1][j]:  # Bottom border
                self.DFS(rows - 1, j, board, visited)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and not visited[i][j]:
                    board[i][j] = "X"
        