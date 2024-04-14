def encrypt(word: str, key: int) -> str:
    result = ""

    ALPHABET_LENGTH = 26
    key = key % ALPHABET_LENGTH

    for char in word:
        new_char = ord(char) + key

        if chr(new_char) > 'z':
            new_char -= ALPHABET_LENGTH

        result += chr(new_char)

    return result


print(encrypt("abc", 1))
print(encrypt("zzz", 1))


def decrypt(encrypted_word: str, key: int) -> str:
    result = ""

    ALPHABET_LENGTH = 26
    key = key % ALPHABET_LENGTH

    for char in encrypted_word:
        new_char = ord(char) - key

        if chr(new_char) < 'a':
            new_char += ALPHABET_LENGTH

        result += chr(new_char)

    return result


print(decrypt("bcd", 1))
print(decrypt("aaa", 1))
