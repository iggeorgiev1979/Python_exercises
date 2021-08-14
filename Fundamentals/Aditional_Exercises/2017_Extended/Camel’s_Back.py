numbers = input().split()
camel = int(input())
stable = True
rounds = 0
while len(numbers) > camel:
    stable = False
    numbers = numbers[1:-1]
    rounds += 1
if not stable:
    print(f"{rounds} rounds\nremaining: {' '.join(numbers)}")
else:
    print(f"already stable: {' '.join(numbers)}")
