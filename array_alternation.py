# 5.8 
def alternate(A):
    for i in range(len(A) - 1):
        if i % 2 == 0:
            if A[i] > A[i + 1]:
                temp  = A[i]
                A[i] = A[i + 1]
                A[i + 1] = temp
        else:
            if A[i] < A[i + 1]:
                temp  = A[i]
                A[i] = A[i + 1]
                A[i + 1] = temp
    return A

