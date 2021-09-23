numbers = input().split()
negative_sum = 0
positive_sum = 0
for num in numbers:
    if int(num) < 0:
        negative_sum += int(num)
    else:
        positive_sum += int(num)

print(negative_sum)
print(positive_sum)

print("The negatives are stronger than the positives") if abs(negative_sum) > positive_sum else print("The positives are stronger than the negatives")
