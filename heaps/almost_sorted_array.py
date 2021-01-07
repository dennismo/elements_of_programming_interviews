# 10.3 Sort an almost sorted array
# each entry in the array is at most k places away from its final sorted position.

# the hint of heap is just too big to

import heapq

def almost_sorted_array(L, k):
    heap = L[:k]
    heapq.heapify(heap)
    result = []
    for n in L[k:]:
        result.append(heapq.heappop(heap))
        heapq.heappush(heap, n)
    for _ in range(k):
        result.append(heapq.heappop(heap))
    return result

print(almost_sorted_array([1,2,4,3], 2))