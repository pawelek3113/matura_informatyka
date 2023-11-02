arr = []
with open("liczby.txt", "r", encoding="UTF-8") as file:
    arr = [list(map(int, line.strip().split(" "))) for line in file.readlines()]

border = max(max(sublist) for sublist in arr) + 1

amounts = [0] * border

for sublist in arr:
    for i in range(len(sublist)):
        number = sublist[i]
        amounts[number] += 1


# Create a list of tuples (number, count)
number_counts = [(i, count) for i, count in enumerate(amounts)]

# Sort the list by count in descending order
number_counts.sort(key=lambda x: x[1], reverse=True)

# Get the first 6 numbers
res = [number for number, count in number_counts[:6]]

res.sort()

print(f"{res[0]};{res[1]};{res[2]};{res[3]};{res[4]};{res[5]}")
