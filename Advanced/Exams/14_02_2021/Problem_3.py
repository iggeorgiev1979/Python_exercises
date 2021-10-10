
def stock_availability(store: list, command: str, *args):
    if command == "delivery":
        store.extend(args)
    elif command == "sell":
        if len(args) == 0:
            return store[1:]
        elif len(args) == 1 and type(args[0]) == int:
            return store[int(args[0]):]
        else:
            for el in args:
                while el in store:
                    store.remove(el)

    return store


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
