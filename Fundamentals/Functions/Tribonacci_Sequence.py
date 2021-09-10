def tribonacci(a):
    tribonacci_list = [1]
    while len(tribonacci_list) < a:
        tribonacci_list.append(sum(tribonacci_list[-3:]))
    return tribonacci_list


number = int(input())
result = tribonacci(number)
print(*result)
