import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    shape = (len(A),len(A[0]))
    B = np.zeros((shape[1],shape[0]))
    for i in range(shape[1]):
        for j in range(shape[0]):
            B[i][j] = A[j][i]
    return B
