class Integer:
    def __init__(self, value: int):
        self.value = value

    @staticmethod
    def convert_from_roman(num):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate(num):
            if (i + 1) == len(num) or roman_numerals[c] >= roman_numerals[num[i + 1]]:
                result += roman_numerals[c]
            else:
                result -= roman_numerals[c]
        return result

    @classmethod
    def from_float(cls, value):
        if not type(value) == float:
            return "value is not a float"
        return cls(int(value))

    @classmethod
    def from_roman(cls, value):
        return cls(cls.convert_from_roman(value))

    @classmethod
    def from_string(cls, value):
        if type(value) == str and value.isnumeric():
            return cls(int(value))
        return "wrong type"


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
