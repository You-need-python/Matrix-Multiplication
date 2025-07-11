# 일반적인 A와 B의 곱셈
def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B.")
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            val = 0
            for k in range(len(B)):
                val += A[i][k] * B[k][j]  #C_ij = A_i1*B_1j + A_i2*B_2j + ... + A_in*B_nj
            row.append(val)
        result.append(row)
    return result
# 분할-정복을 이용한 A와 B의 곱셈
# A와 B는 2^n x 2^n 행렬이어야 함
def matrix_multiply_DAC(A, B): # divide and conquer
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B.")

    def add_matrix(X, Y):
        return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

    def DAC(A, B):
        n = len(A)
        if n == 1:
            return [[A[0][0] * B[0][0]]]
        mid = n // 2
        # Divide matrices into quadrants
        A11 = [row[:mid] for row in A[:mid]]
        A12 = [row[mid:] for row in A[:mid]]
        A21 = [row[:mid] for row in A[mid:]]
        A22 = [row[mid:] for row in A[mid:]]
        B11 = [row[:mid] for row in B[:mid]]
        B12 = [row[mid:] for row in B[:mid]]
        B21 = [row[:mid] for row in B[mid:]]
        B22 = [row[mid:] for row in B[mid:]]
        # Compute submatrices
        C11 = add_matrix(DAC(A11, B11), DAC(A12, B21))
        C12 = add_matrix(DAC(A11, B12), DAC(A12, B22))
        C21 = add_matrix(DAC(A21, B11), DAC(A22, B21))
        C22 = add_matrix(DAC(A21, B12), DAC(A22, B22))
        # Combine submatrices
        top = [c11 + c12 for c11, c12 in zip(C11, C12)]
        bottom = [c21 + c22 for c21, c22 in zip(C21, C22)]
        return top + bottom

    return DAC(A, B)
A = [
    [1, 0],
    [0, 1]
]
B = [
    [5, 6],
    [7, 8]
]

product = matrix_multiply(A, B)
for row in product:
    print(row)

print('-'*20)

product_DAC = matrix_multiply_DAC(A, B)
for row in product_DAC:
    print(row)