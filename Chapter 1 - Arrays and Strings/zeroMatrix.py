# Natural Solution

def zero(matrix):
    colums = []
    rows = []
    for i in range(len(matrix)):
        rows.append(True)
    for i in range(len(matrix[0])):
        colums.append(True)

    for i in range(len(matrix)):
        if rows[i]:
            for j in range(len(matrix[0])):
                if colums[j]:
                    if matrix[i][j] == 0:
                        rows[i] = False
                        colums[j] = False
                        break

    for i in range(len(rows)):
        if not rows[i]:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

    for i in range(len(colums)):
        if not colums[i]:
            for j in range(len(matrix)):
                matrix[j][i] = 0

# Tests

matrix = [
    [2, 3, 4, 5, 6],
    [3, 0, 5, 6, 7],
    [2, 3, 4, 1, 6],
    [2, 3, 4, 5, 6]
]

zero(matrix)

for i in matrix:
    print(i)


    
