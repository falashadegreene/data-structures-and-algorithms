def quick_sort(arr, left, right):

    if left < right:
        pos = partition(arr, left, right)
        quick_sort(arr, left, pos - 1)
        quick_sort(arr, right, pos + 1)


def partition(arr, left, right):

    piv = arr[right]
    low = left - 1
    for i in range(left, right):
        if arr[i] <= piv:
            low += 1
            swap(arr, i, low)

    swap(arr, right, low + 1)
    return low + 1


def swap(arr, i, low):
    
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp
