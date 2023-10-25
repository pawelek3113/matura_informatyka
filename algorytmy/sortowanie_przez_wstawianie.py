def insertion_sort(seq: list[int]) -> None:
    n: int = len(seq)

    for i in range(1, n):
        current: int = seq[i]

        # start comparing from previous item
        j: int = i - 1

        while seq[j] > current and j >= 0:
            # shift (copy) the previous item to the right side
            seq[j+1] = seq[j]
            j -= 1

        seq[j+1] = current


array: list[int] = [6, 4, 5, 7, 2]
insertion_sort(array)

print(array)
