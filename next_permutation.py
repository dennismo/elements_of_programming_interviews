# 1 3 2 0
# 2 0 1 3
def nextPermutation(l):
    position = -1
    for i in reversed(range(1, len(l))):
        if l[i - 1] < l[i]:
            position = i - 1
            break
    if position == -1
        return []
    smallest = float("inf")
    smallest_index = 0
    for i in range(position, len(l)):
        if l[i] > position and l[i] < smallest:
            smallest = l[i]
            smallest_index = i
    l[smallest_index] = l[position]
    l[position] = smallest
    l[position + 1:] = reversed(l[position + 1:])