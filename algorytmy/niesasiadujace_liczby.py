"""
Maximum non-adjacent sum
-----
TASK: Calculate the maximum sum of non-adjacent numbers

examples:
    numbers = [10, 3, 5, 2, 6]
    max_sum = 10 + 5 + 6 = 21;

    numbers = [2, 1, 2, 7, 3]
    max_sum = 2 + 7 = 9;

-----
1. Create result_array; its length is the same as nums_array's
2. result_array represents sums; its last element is the maximum sum of non-adjacent numbers
3. result_array[0] = nums_array[0]; result_array[1] = max(nums_array[0], nums_array[1])
4. Iterate over indexes from 2 to len(nums_array)
    5. result_array[index] = max(result_array[index - 1], result_array[index - 2] + nums_array[index])
6. Return the last element of result_array - final sum

-----
Maksymalna suma niesąsiadujących elementów

1. Stworz liste result_array, której liczba elementów wynosi tyle samo co liczba elementów nums
2. result_array reprezentuje kolejne sumy; jej ostatnim elementem jest maksymalna suma niesąsiadujących liczb
3. result_array[0] = nums_array[0]; result_array[1] = max(nums_array[0], nums_array[1])
4. Zrób pętlę iterującą po liczbach od 2 do len(nums_array), będącymi indeksami elementów
    5. result_array[index] = max(result_array[index - 1], result_array[index - 2] + nums_array[index])
6. Zwróć ostatni element result_array - końcowa suma
"""


def get_max_non_adjacent_sum(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0

    res: list[int] = [0] * len(nums)

    res[0] = nums[0]
    res[1] = max(nums[0], nums[1])

    for index in range(2, len(nums)):
        res[index] = max(res[index - 1], res[index - 2] + nums[index])

    return res[-1]


example_array = [10, 5, 2, 6, 4]

max_sum = get_max_non_adjacent_sum(example_array)
print(f"The maximum sum of non-adjacent elements of {example_array} is: {max_sum}")
