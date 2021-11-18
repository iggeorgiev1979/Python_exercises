def get_primes(list_of_integers):
    for number in list_of_integers:
        if number > 1:
            is_prime = True
            for num in range(2, number + 1):
                if not number == num and number % num == 0:
                    is_prime = False
                    break
            if is_prime:
                yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0, 11])))
