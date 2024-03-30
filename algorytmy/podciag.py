# find the longest subsequence where sum of elements is 10
# use the caterpillar method

def find_subsequence(sequence: list[int]):
    WANTED_SUM = 10

    head = 0
    tail = 0

    max_sequence = []
    sequences = []
    while head < len(sequence):
        current_subsequence = sequence[tail:head+1]
        current_sum = sum(current_subsequence)

        if current_sum < WANTED_SUM:
            head += 1
        elif current_sum > WANTED_SUM:
            tail += 1
        elif current_sum == WANTED_SUM:
            sequences.append(current_subsequence)

            if len(max_sequence) < len(current_subsequence):
                max_sequence = current_subsequence
            head += 1

    print(f"sequences: {sequences}")
    return max_sequence


print(find_subsequence([1, 4, 5, 3, 7, 2]))
