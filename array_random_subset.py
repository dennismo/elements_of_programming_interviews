import random
random.seed(42)


def arrayRandomPerm(A):
    for i in range(len(A)):
        rnum = random.random() % (len(A) - i)
        A[i], A[rnum + i] = A[rnum + i], A[i]
        

        