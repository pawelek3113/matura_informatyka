shares = []
with open("gielda.txt", "r", encoding="UTF-8") as file:
    shares = [int(share) for share in file.read().split()]

smallest = min(shares)
i_smallest = shares.index(smallest)
new_shares = shares[i_smallest:]

biggest = max(new_shares)
i_biggest = new_shares.index(biggest) + len(shares[:i_smallest])

profit = (biggest - smallest)*100_000

# indexes start from zero
buying_day = i_smallest + 1
selling_day = i_biggest + 1

# print(f"Index of the smallest value ({smallest}): {i_smallest}")
# print(f"Index of the biggest value ({biggest}): {i_biggest}")
# print(f"Profit: {profit}")

print(f"{buying_day};{selling_day};{profit};")
