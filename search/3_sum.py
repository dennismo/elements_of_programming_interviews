def has_two_sum(A, k):
    start, end = 0, len(A) - 1
    while start <= end:
        if A[start] + A[end] > k:
            end -= 1
        elif A[start] + A[end] < k:
            start += 1
        else:
            return True
    return False

def has_three_sum(A, k):
    A.sort()
    return any(has_two_sum(A, k - a_val) for a_val in A)