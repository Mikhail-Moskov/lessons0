def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        colum = []
        matrix.append(colum)
        for j in range(m):
            colum.append(value)
    return matrix

print(get_matrix(3, 4, 5))
