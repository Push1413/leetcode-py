def setZeroes(matrix):
    row = len(matrix)
    col = len(matrix[0])

    first_row_zero = any(matrix[0][j] == 0 for j in range(col))
    first_col_zero = any(matrix[i][0] == 0 for i in range(row))

    for i in range(1,row):
        for j in range(1,col):
            if matrix[i][j] == 0:
                matrix[0][j] =0
                matrix[i][0] =0

    for r in range(1,row):
        for c in range(1,col):
            if matrix[0][c]==0 or matrix[r][0]==0:
                matrix[r][c]=0

    if first_row_zero:
        for j in range(col):
            matrix[0][j] = 0

    # Handle the first column
    if first_col_zero:
        for i in range(row):
            matrix[i][0] = 0

    for i in range(row):
        for j in range(col):
            print(matrix[i][j],end=" ")
        print()



if __name__ == '__main__':
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    setZeroes(matrix)