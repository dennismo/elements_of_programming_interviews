#12.5

def closest_twin(arr):
    s = dict()
    min_val = float('inf')
    for i in range(len(arr)):
        if arr[i] in s:
            min_val = min(i - s[arr[i]], min_val)
        s[arr[i]] = i
    return min_val