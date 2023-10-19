def get_int_list(file_name: str) -> list[int]:
    with open(file_name, "r", encoding="UTF-8") as file:
        max_distances = [int(num) for num in file.read().split()]
        return max_distances


def get_max_non_adjacent_sum(nums: list[int]):
    if len(nums) == 0:
        return 0

    res = [0] * len(nums)

    res[0] = nums[0]
    res[1] = max(nums[0], nums[1])

    for index in range(2, len(nums)):

        res[index] = max(res[index - 1], res[index - 2] + nums[index])

    return res[-1]


list_of_numbers = get_int_list("rower.txt")

print(get_max_non_adjacent_sum(list_of_numbers))
