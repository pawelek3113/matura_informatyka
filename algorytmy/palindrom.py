# palindrom - wyraz czytany od lewej i od prawej wygląda tak samo

# def is_palindrom(word) -> bool:
#     return word == word[::-1]

def is_palindrom(word) -> bool:
    for i in range(len(word)//2):
        if word[i] != word[len(word)-1-i]:
            return False

    return True


print(is_palindrom("kajak"))
print(is_palindrom("kok"))
print(is_palindrom("kot"))



