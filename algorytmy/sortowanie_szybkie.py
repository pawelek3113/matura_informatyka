def quicksort(array: list[int], start=0, end=None) -> None:
    if end is None:
        end = len(array) - 1
    if start >= end or start < 0 or end >= len(array):
        return

    pivot: int = partition(array, start, end)
    # pass partitions recursively into quicksort function
    quicksort(array, start, pivot-1)
    quicksort(array, pivot+1, end)


def partition(array: list[int], start, end) -> int:
    # returns location of pivot
    # set pivot at the end
    pivot: int = array[end]
    i: int = start - 1

    for j in range(start, end):
        if array[j] < pivot:
            i += 1
            # swap
            array[i], array[j] = array[j], array[i]
        else:
            j += 1

    i += 1
    # final pivot position
    temp: int = array[i]
    array[i] = array[end]
    array[end] = temp

    return i


seq: list[int] = [8, 2, 5, 3, 9, 4, 7, 6, 1]

quicksort(seq, 0)
print(seq)
