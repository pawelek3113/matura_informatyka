# divide and conquer sorting algorithm
# merge sort

def _merge(lst1: list, lst2: list):
    sorted_lst = []
    left_size = len(lst1)
    right_size = len(lst2)

    l = 0
    r = 0

    while l < left_size and r < right_size:
        if lst1[l] < lst2[r]:
            sorted_lst.append(lst1[l])
            l += 1
        else:
            sorted_lst.append(lst2[r])
            r += 1

    while l < left_size:
        sorted_lst.append(lst1[l])
        l += 1

    while r < right_size:
        sorted_lst.append(lst2[r])
        r += 1

    return sorted_lst


def merge_sort(lst: list):
    # non-mutating version of mergesort
    if len(lst) < 2:
        return lst.copy()

    mid_idx = len(lst)//2

    left_sorted = merge_sort(lst[:mid_idx])
    right_sorted = merge_sort(lst[mid_idx:])

    return _merge(left_sorted, right_sorted)


arr = []

with open("liczby.txt", "r", encoding="UTF-8") as f:
    arr = [int(x) for x in f.read().split(" ")]

sorted_arr = merge_sort(arr)

print(sorted_arr[len(sorted_arr)//2 - 1])
