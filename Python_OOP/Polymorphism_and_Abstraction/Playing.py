class Guitar:
    def play(self):
        return "Playing the guitar"


def start_playing(arg):
    return arg.play()


guitar = Guitar()
print(start_playing(guitar))
