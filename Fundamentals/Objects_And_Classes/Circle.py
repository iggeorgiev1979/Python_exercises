class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return self.__pi * 2 * (self.diameter / 2)

    def calculate_area(self):
        return self.__pi * ((self.diameter / 2) ** 2)

    def calculate_area_of_sector(self, angle):
        self.angle = angle
        return (self.__pi * ((self.diameter / 2) ** 2)) * (self.angle / 360)
