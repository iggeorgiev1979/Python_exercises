class Planet:
    def __init__(self, name: str):
        self.name = name
        self.items = []
        self.counter = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        striped_value = value.strip()
        if not striped_value:
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value

