def find_pattern(word: str, pattern: str):
    occurences = []
    found = True

    for i in range(0, len(word)):
        if word[i] == pattern[0]:
            idx = i
            for j in range(1, len(pattern)):
                if word[i+j] != pattern[j]:
                    found = False

            if found:
                occurences.append(idx)

    print(occurences)


find_pattern("i like dogs, especially white dogs", "dogs")
find_pattern("loving cats is my life, cats are truly amazing!", "cats")

