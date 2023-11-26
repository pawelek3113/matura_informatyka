"""Problem wydawania reszty"""


def give_change(amount: int, available_coins: list[int]) -> list[int]:
    available_coins.sort(reverse=True)

    n = amount

    coins = []

    i = 0
    while i <= len(available_coins)-1:
        if available_coins[i] <= n:
            coins.append(available_coins[i])
            n -= available_coins[i]
        else:
            i += 1

    return coins


a_coins = [2, 1, 3, 7]
amount_to_pay = int(input())
print(give_change(amount_to_pay, a_coins))

