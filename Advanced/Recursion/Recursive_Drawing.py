def draw(n: int):
    if n == 0:
        return
    print(n * "*")
    draw(n - 1)
    print(n * "#")


draw(5)
