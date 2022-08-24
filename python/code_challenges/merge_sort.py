# convert pseudo-code into working code by creating a visual step through of each array.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
