def insertion_sort(arr):
    i = 1
    n = len(arr)
    while i < n:
        key = arr[i]
        m = i - 1
        while m >= 0 and arr[m] > key:
            arr[m+1] = arr[m]
            m -= 1
        arr[m+1] = key
        i += 1
    return arr