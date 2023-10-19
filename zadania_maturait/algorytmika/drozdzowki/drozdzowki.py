def binary_search(x: int, seq: list[int]):
    beg_idx = 0
    end_idx = len(seq) - 1

    while beg_idx < end_idx:
        mid_idx = (beg_idx + end_idx)//2

        if x < seq[mid_idx]:
            beg_idx = mid_idx + 1
        elif x >= seq[mid_idx]:
            end_idx = mid_idx

    if x == seq[beg_idx]:
        return beg_idx + 1
    else:
        return -1


prices: list[int] = []

with open("drozdzowki.txt", "r", encoding="UTF-8") as file:
    prices = [int(price) for price in file.read().split()]

# print(prices[10000-1219])
# print(10000-1219)

# NIEROSNĄCY CIĄG; RÓŻNICA!!!
prices.sort(reverse=True)

cash: int = 50000

affordable_prices: list[int] = []

for price in prices:
    if price < cash:
        affordable_prices.append(price)

the_most_expensive: int = max(affordable_prices)

wanted_idx = binary_search(the_most_expensive, prices)

print(f"{wanted_idx};{the_most_expensive}")
