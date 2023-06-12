def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)

def merge(arr, start, mid, end):

    n1 = mid - start + 1
    n2 = end - mid

    L = [arr[start + i] for i in range(n1)]
    R = [arr[mid + i + 1] for i in range(n2)]

    L.append(float('inf'))
    R.append(float('inf'))

    i, j = 0, 0
    
    for k in range(start, end+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1