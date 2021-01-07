# 4.2
import math

def swapBits(num, i ,j):
    i_th_bit = num & (2 ** i)
    j_th_bit = num & (2 ** j)
    num &= ~(2 ** i + 2 ** j)
    num += i_th_bit * 2 ** j + j_th_bit * 2 ** i
    return num

print(swapBits(1, 0, 3))
