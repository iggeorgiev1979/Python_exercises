def my_function(a):
    if a < 3:
        return 'Fail'
    elif 3 <= a < 3.5:
        return 'Poor'
    elif 3.5 <= a < 4.5:
        return 'Good'
    elif 4.5 <= a < 5.5:
        return 'Very Good'
    elif 5.5 <= a <= 6:
        return 'Excellent'


grade = float(input())
print(my_function(grade))