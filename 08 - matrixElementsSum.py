def matrixElementsSum(matrix):
    sum = 0
    for i in range(1,len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i - 1][j] == 0:
                matrix[i][j] = 0
    for i in matrix:
        for j in i:
            sum += j
    return sum 
