def linear_search(arr, num):
    n = len(arr)
    for i in range(n):
        if arr[i] == num:
            return i