class EncryptionGenerator:
    def __init__(self, text: str):
        self.text = text

    def __add__(self, other):
        if not self._is_number(other):
            raise ValueError("You must add a number.")
        return self._encrypt(other)

    @staticmethod
    def _is_number(symbol):
        return type(symbol) == int

    def _encrypt(self, number: int):
        result = ""
        for el in self.text:
            result += chr(self.generate_the_ascii_code(el, number))
        return result

    @staticmethod
    def generate_the_ascii_code(symbol: str, number):
        index = ord(symbol) - 32
        new_index = (index + number) % 95
        return 32 + new_index


example = EncryptionGenerator('Super-Secret Message')
print(example + 20)
print(example + -52)
