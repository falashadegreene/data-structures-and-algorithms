def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        ind = i - 1

        while ind >= 0:
            if array[ind] > temp:
                array[ind+1] = array[ind]
                ind = ind - 1
            else:
                break
        array[ind+1] = temp
    return array
