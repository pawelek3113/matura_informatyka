def naive_search(a: list, b: list):
    for j in range(len(b)):
        is_found = False

        for i in range(len(a)):
            if a[i] == b[j]:
                is_found = True

        if is_found:
            print(f"{b[j]} found")


seq = [1, 2, 3, 4, 5, 6, 7, 8]
find = [5, 10, 29, 1, 7]

naive_search(seq, find)
# 5 found
# 1 found
# 7 found
