from random import randint


def counting_sort(array: list[int]) -> list[int]:
    if len(array) == 0:
        return array

    border = max(array)
    # array containing amounts of occurrences of numbers
    amounts: list[int] = [0] * (border + 1)

    for i in range(len(array)):
        num = array[i]
        amounts[num] += 1

    sorted_array = []

    for i in range(0, len(amounts)):
        if amounts[i] == 0:
            continue
        else:
            for j in range(amounts[i]):
                sorted_array.append(i)

    return sorted_array


# seq: list[int] = [4, 6, 4, 5, 0, 7, 6, 2, 3]
seq = []
for _ in range(randint(0, 35)):
    seq.append(randint(0, 100))
sorted_seq: list[int] = counting_sort(seq)

print(seq)
print(sorted_seq)
