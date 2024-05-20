class ReversePolishNotation:
    def __init__(self, postfix_equation: str):
        if postfix_equation == "":
            raise Exception("The equation is empty")
        self.equation = postfix_equation

    def calculate(self):
        stack = []

        counter = 0
        for char in self.equation:
            if char.isdigit():
                counter += 1
                stack.append(char)
            elif char in ["+", "*"]:
                result = eval(f"{stack.pop()} {char} {stack.pop()}")
                stack.append(result)
            elif char in ["-", "/", "%"]:
                second = stack.pop()
                first = stack.pop()

                result = eval(f"{first} {char} {second}")
                stack.append(result)
            else:
                raise Exception("Wrong operator")

        result = stack.pop()
        return result

    @property
    def result(self):
        return self.calculate()


eq = ReversePolishNotation("234*+45*56*/-")
print(eq.result)
