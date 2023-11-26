def give_change(r: int, a_coins: list[int]) -> list[int]:
    n = r
    a_coins.sort(reverse=True)

    coins = []

    i = 0
    while i < len(a_coins) - 1:
        if a_coins[i] <= n:
            coins.append(a_coins[i])
            n -= a_coins[i]
        else:
            i += 1

    return coins


available_coins = [1, 2, 5, 10]

rest = 500 - 123

change = give_change(rest, available_coins)

change.sort(reverse=True)

print(";".join(map(str, change)))
