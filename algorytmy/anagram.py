# anagram - wyraz powstały przez przestawienie liter innego wyrazu
# sprawdzamy czy ilość poszczególnych liter pierwszego wyrazu jest równa liczbie liter drugiego

def _count_characters(word):
    characters = {}
    for char in word:
        characters[char] = characters.get(char, 0) + 1

    return characters


def is_anagram(w1, w2) -> bool:

    w1_characters = _count_characters(w1)
    w2_characters = _count_characters(w2)

    return w1_characters == w2_characters


print(is_anagram("listen", "silent"))
print(is_anagram("dzielenia", "niedziela"))
print(is_anagram("dog", "hog"))
