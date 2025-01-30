def rotate(matrix):
    # Transpose and reverse rows using zip
    matrix[:] = [list(row) for row in zip(*matrix[::-1])]
    for row in matrix:
        print(row)

def rotate2(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    for row in matrix:
        print(row)

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(matrix)
    print()
    rotate2(matrix1)