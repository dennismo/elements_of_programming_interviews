"""
Given n and m
Define a good number to be the summation of powers of m
So if m =3
Good numbers can be 1+3 or 1+ 9 or so on
Find the smallest good number  greater than n
"""
def nice_number(n, m):
    k, s = 0, 0
    while s < n:
        s += m^k
        k += 1
    
    for i in reversed(range(k)):
        if s - i^m > n:
            s - i^m
    return s
