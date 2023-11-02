def merge_sort(array: list[int]):
    length: int = len(array)
    if length <= 1:
        return

    middle: int = length//2
    left_array: int = array[:middle]
    right_array: int = array[middle:]

    merge_sort(left_array)
    merge_sort(right_array)
    merge(left_array, right_array, array)


def merge(left_array: list[int], right_array: list[int], array: list[int]):
    left_size: int = len(array)//2
    right_size: int = len(array) - left_size
    i: int = 0
    l: int = 0
    r: int = 0

    while l < left_size and r < right_size:
        if left_array[l] < right_array[r]:
            array[i] = left_array[l]
            i += 1
            l += 1
        else:
            array[i] = right_array[r]
            i += 1
            r += 1

    while l < left_size:
        array[i] = left_array[l]
        i += 1
        l += 1

    while r < right_size:
        array[i] = right_array[r]
        i += 1
        r += 1


seq: list[int] = [3, 6, 7, 2, 1, 3, 5, 9, 2, 0]
merge_sort(seq)
print(seq)
