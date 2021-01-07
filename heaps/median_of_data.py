# 10.5
'''
You want to compute the running median of a sequence of numbers. The sequence is presented to you in a streaming
fashion-you carmot back up to read an earlier value, and you need to output the median after reading in each new element.
For example, if the input is 1,0,3,5,2,0,1 the output is 1,0.5,1,2,2,1.5,1


use 2 heaps
'''
import heapq

def median_of_running_data(L):
    minHeap = [L[1] if L[0] < L[1] else L[0]]
    maxHeap = [L[0] if L[0] < L[1] else L[1]]
    # state: -1, 0, 1
    # -1 = minHeap have more
    # 1 = maxHeap have more
    # 0 = both equal
    state = 0
    medians = [L[0], (L[0] + L[1])/2]

    for n in L[2:]:
        if n < maxHeap[0]:
            if state == 1:
                temp = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, temp)
                heapq.heappush(maxHeap, n)
            elif state == 0:
                heapq.heappush(maxHeap, n)
                state = 1
            elif state == -1:
                heapq.heappush(maxHeap, n)
                state = 0
        elif n > minHeap[0]:
            if state == -1:
                temp = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, temp)
                heapq.heappush(minHeap, n)
            if state == 0:
                heapq.heappush(minHeap, n)
                state = -1
            if state == 1:
                heapq.heappush(minHeap, n)
                state = 0
        if state == -1:
            medians.append(minHeap[0])
        elif state == 0:
            medians.append((minHeap[0] + maxHeap[0]) * 0.5)
        else:
            medians.append(maxHeap[0])
        print(minHeap)
        print(maxHeap)
        print(state)
    return medians

print(median_of_running_data([1,0,3,5,2,0,1]))



