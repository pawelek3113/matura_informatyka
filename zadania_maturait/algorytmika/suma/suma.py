# dlugosc najkrotszego spojnego podciagu o sumie elementow rownej 10

def find_shortest_sequence(sequence: list[int]):
    WANTED_SUM = 10

    head = 0
    tail = 0

    shortest_length = len(sequence) + 20

    while head < len(sequence):
        current_sequence = sequence[tail:head+1]
        current_sum = sum(current_sequence)

        if current_sum < 10:
            head += 1
        elif current_sum > 10:
            tail += 1
        elif current_sum == 10:
            head += 1
            if shortest_length > len(current_sequence):
                shortest_length = len(current_sequence)

    if shortest_length > len(sequence):
        shortest_length = 0
    return shortest_length


seq = [1, 4, 5, 3, 7, 2]
print(find_shortest_sequence(seq))
