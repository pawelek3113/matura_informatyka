def binary_search(number_to_find, seq):
    begin_idx = 0
    end_idx = len(seq) - 1

    while begin_idx < end_idx:
        mid_idx = (begin_idx + end_idx) // 2
        if number_to_find > seq[mid_idx]:
            begin_idx = mid_idx + 1
        elif number_to_find <= seq[mid_idx]:
            end_idx = mid_idx

    return seq[begin_idx] == number_to_find


sequence = [1, 2, 3, 4, 6, 7, 9, 12, 20, 21]

n = int(input("How many numbers would you like to find?"))

find: list[int] = []

for i in range(n):
    find.append(int(input(f"{i+1}. ")))

for number in set(find):
    if binary_search(number, sequence):
        print(f"{number} found")
    else:
        print(f"{number} not found :(")
