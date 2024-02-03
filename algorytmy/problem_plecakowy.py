def knapsack_problem_max_value(weights: list, values: list, max_weight: int):
    # number of items
    n = len(weights)
    # initialize an array to store maximum values for different knapsack weights
    dp = [0] * (max_weight + 1)

    # loop over items
    for i in range(n):
        # loop over weights in reverse order (from maximum to the minimum which is the weight of current item)
        for j in range(max_weight, weights[i] - 1, -1):
            # finding and updating the max value for knapsack of weight j
            # dp[j] is the current max value of knapsack of mass j
            # dp[j - weights[i]] + values[i] is the value of knapsack of weight j including the i-th item
            # dp[j - weights[i]] is the value of knapsack excluding the i-th item
            print(f"{dp[j]} vs {dp[j - weights[i]]} + {values[i]}")
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
            print(dp)

    # return the max possible value
    return dp[max_weight]


# example
max_weight = 8
# [first_item, second_item, third_item]
weights = [3, 5, 8]
values = [1, 3, 7]

result = knapsack_problem_max_value(weights, values, max_weight)
print(result)
