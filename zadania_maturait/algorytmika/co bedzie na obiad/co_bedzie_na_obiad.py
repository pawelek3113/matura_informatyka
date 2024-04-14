KEY = 21
ENCRYPTED_MSG = "fjogzot hdzgjiz"


def decrypt(encr: str, key: int) -> str:
    ALPHABET_LENGTH = 26

    key = key % ALPHABET_LENGTH

    result = ""

    for char in encr:
        if char == " ":
            result += " "
            continue

        new_char = ord(char) - key

        if chr(new_char) < 'a':
            new_char += ALPHABET_LENGTH

        result += chr(new_char)

    return result


print(decrypt(ENCRYPTED_MSG, KEY))