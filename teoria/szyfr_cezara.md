# Szyfr cezara
___

Szyfr Cezara jest szyfrem podstawieniowym, oznacza to że każdy znak tekstu jawnego zastępujemy innym znakiem przy szyfrowaniu. 
W szyfrze Cezara stosujemy przesunięcie. Powiedzmy że przesunięcie tego szyfru to 5. 
Przesunięcie określa odległość w alfabecie między literą w tekście jawnym, a literą w tekście zaszyfrowanym.

---

```python
print(ord('a')) # 97
print(chr(97)) # a
```

---

Gdy użytkownik poda klucz dłuższy od alfabetu wystarczy zastosować:
```python
key: int = key % ALPHABET_LENGTH

# key?=3
# 3 % 26 = 3

# key?=29
# 29 % 26 = 3
```

### Szyfrowanie
Do każdego znaku wyrazu dodajemy klucz.
Pamiętamy o zawijaniu alfabetu, gdy wyskoczymy poza granice.

```python
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
```

### Odszyfrowanie
Od każdego znaku wyrazu odejmujemy klucz.
Pamiętamy o zawijaniu alfabetu, gdy wyskoczymy poza granice.

```python
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
```