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

def add_matrix(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
def sub_matrix(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

# 분할-정복을 이용한 A와 B의 곱셈
# A와 B는 2^n x 2^n 행렬이어야 함

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

# Strassen 알고리즘을 이용한 A와 B의 곱셈
# A와 B는 2^n x 2^n 행렬이어야 함

def Strassen(A, B):
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
    # Compute M1 to M7
    M1 = Strassen(add_matrix(A11, A22), add_matrix(B11, B22))  # M1 = (A11 + A22)(B11 + B22)
    M2 = Strassen(add_matrix(A21, A22), B11)  # M2 = (A21 + A22)B11
    M3 = Strassen(A11, sub_matrix(B12, B22)) #M3 = A11(B12 - B22)
    M4 = Strassen(A22, sub_matrix(B21, B11)) #M4 = A22(B21 - B11)
    M5 = Strassen(add_matrix(A11, A12), B22)  # M5 = (A11 + A12)B22
    M6 = Strassen(sub_matrix(A21, A11), add_matrix(B11, B12))  # M6 = (A21 - A11)(B11 + B12)
    M7 = Strassen(sub_matrix(A12, A22), add_matrix(B21, B22))  # M7 = (A12 - A22)(B21 + B22)
    # Compute submatrices
    C11 = add_matrix(sub_matrix(add_matrix(M1, M4), M5), M7)  # C11 = M1 + M4 - M5 + M7
    C12 = add_matrix(M3, M5)  # C12 = M3 + M5
    C21 = add_matrix(M2, M4)  # C21 = M2 + M4
    C22 = add_matrix(sub_matrix(add_matrix(M1, M3), M2), M6)  # C22 = M1 - M2 + M3 + M6
    # Combine submatrices
    top = [c11 + c12 for c11, c12 in zip(C11, C12)]
    bottom = [c21 + c22 for c21, c22 in zip(C21, C22)]
    return top + bottom

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

product_DAC = DAC(A, B)
for row in product_DAC:
    print(row)

print('-'*20)

product_Strassen = Strassen(A, B)
for row in product_Strassen:
    print(row)