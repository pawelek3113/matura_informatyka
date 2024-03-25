first = ""
second = ""

with open("2liczby.txt", "r", encoding="UTF-8") as file:
    first, second = file.read().split(" ")


counter = 0

for i in range(len(first) - 2):
    if first[i: i+3] == second:
        counter += 1

print(counter)