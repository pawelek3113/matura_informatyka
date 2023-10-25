stars: list[int] = []
with open("kawiarnie.txt", "r", encoding="UTF-8") as file:
    stars = [int(review) for review in file.read().split()]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1

        current = arr[i]
        while arr[j] > current and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current


insertion_sort(stars)

res: list[int] = stars[-5:len(stars)]

for review in res:
    print(review, end=";")
