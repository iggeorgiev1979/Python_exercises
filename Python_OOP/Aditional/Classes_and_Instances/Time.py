class Time:
    max_hours = 24
    max_minutes = 60
    max_seconds = 60

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    @property
    def hours(self):
        return self.__hours
    
    @hours.setter
    def hours(self, value):
        if value >= self.max_hours:
            value -= self.max_hours
        self.__hours = value
    
    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value):
        if value >= self.max_minutes:
            value -= self.max_minutes
            self.hours += 1
        self.__minutes = value
    
    @property
    def seconds(self):
        return self.__seconds
    
    @seconds.setter
    def seconds(self, value):
        if value >= self.max_seconds:
            value -= self.max_seconds
            self.minutes += 1
        self.__seconds = value

    def set_time(hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    @staticmethod
    def stringify(value):
        if value < 10:
            return f"0{value}"
        return f"{value}"
    

    def get_time(self):
        return f"{self.stringify(self.hours)}:{self.stringify(self.minutes)}:{self.stringify(self.seconds)}"

    def next_second(self):
        self.seconds += 1
        return self.get_time()

# time = Time(10, 59, 59)
# print(time.next_second())
    
    