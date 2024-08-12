N, B = map(int, input().split())

matrix = [ list(map(int, input().split())) for _ in range(N)]

def pow_matrix(matrix, exp):
    if exp == 1:
        return matrix
    elif exp == 2:
        return multip_matrix(matrix, matrix)
    
    calced_matrix = pow_matrix(matrix, exp >> 1)
    if exp % 2 == 0:
        return multip_matrix(calced_matrix, calced_matrix)
    else : 
        return multip_matrix(multip_matrix(calced_matrix, calced_matrix), matrix)

    
def multip_matrix(matrix1, matrix2):
    length = len(matrix1)
    result = [ [0] * length for _ in range(length)]

    for r in range(length) :
        for c in range(length) :
            result[r][c] = sum([ matrix1[r][i] * matrix2[i][c] for i in range(length)]) % 1000

    return result

result_matrix = pow_matrix(matrix, B)

for i in range(N):
    for j in range(N):
        result_matrix[i][j] %= 1000

for row in result_matrix : print(' '.join(map(str, row)))