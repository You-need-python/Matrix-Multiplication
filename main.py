# 정사각행렬 A와 B의 곱셈
def matrix_multiply(A, B):
    # 곱셈 가능 여부 확인
    if len(A[0]) != len(B):
        raise ValueError("A의 열의 수와 B의 행의 수가 다름.")
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

A = [
    [1, 2, 3],
    [4, 5, 6]
]
B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

product = matrix_multiply(A, B)
for row in product:
    print(row)