def find_coins(coins: list, value: int):
    result = {}
    for index in range(len(coins) - 1, -1, -1):
        coin = coins[index]
        if coin <= value:
            tmp = value // coin
            value = value % coin
            result[coin] = tmp

        if value == 0:
            return result
    return "Error"


print(find_coins([3, 7], 11))
print(find_coins([1, 2, 5, 10, 20, 50], 923))
