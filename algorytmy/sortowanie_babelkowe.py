def bubble_sort(seq: list[int]) -> None:
    n: int = len(seq)

    for i in range(n-1):
        for j in range(n-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]


array: list[int] = [6, 4, 5, 7, 2]
bubble_sort(array)

print(array)
