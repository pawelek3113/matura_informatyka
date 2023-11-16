def is_prime(num: int) -> bool:
    k = 2
    while k*k <= num:
        if num % k == 0:
            return False
        k += 1

    return True


def get_prime_numbers(arr: list[int]) -> list[bool]:
    res: list[bool] = []
    for number in arr:
        if is_prime(number):
            res.append(True)
        else:
            res.append(False)

    return res


class Solution:
    def __init__(self, file):
        self.file = file
        self.content = self.read_file()
        self.result = self.format_result()

    def read_file(self) -> list[int]:
        with open(self.file, "r", encoding="UTF-8") as file:
            content = [int(n) for n in file.read().split(" ")]
            return content

    def get_result(self):
        res: list[str] = ["TAK" if s is True else "NIE" for s in get_prime_numbers(self.content)]
        return res

    def format_result(self) -> str:
        return ";".join(self.get_result())


s = Solution("liczby.txt")
print(s.result)
