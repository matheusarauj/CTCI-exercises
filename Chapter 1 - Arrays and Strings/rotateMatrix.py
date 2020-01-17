# Natural Solution

def rotate(matrix):
    if(len(matrix) == 0 or len(matrix) != len(matrix[0])):
        return False
    
    n = len(matrix)
    for layer in range(int(n/2)):
        first = layer
        last = n - 1 - layer
        for i in range(first, last, 1):
            offset = i - first
            top = matrix[first][i]

            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
    
    return top


# Test

matrix = [
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0]
]

rotate(matrix)
for i in matrix:
    print(i)