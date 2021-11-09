class EncryptionGenerator:
    def __init__(self, text: str):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("You must add a number.")

        result = ""
        for el in self.text:
            index = ord(el) - 32
            new_index = (index + other) % 95
            result += chr(32 + new_index)
        return result


example = EncryptionGenerator('Super-Secret Message')
print(example + 20)
print(example + -52)
