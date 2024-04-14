KEY = 13
MESSAGE = "i love hacking bro"


def encrypt(word: str, key: int) -> str:
    ALPHABET_LENGTH = 26

    result = ""

    key = key % ALPHABET_LENGTH

    for char in word:
        if char == " ":
            result += " "
            continue
        new_char = ord(char) + key

        if chr(new_char) > 'z':
            new_char -= ALPHABET_LENGTH

        result += chr(new_char)

    return result


print(encrypt(MESSAGE, KEY))
