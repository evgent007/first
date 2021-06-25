def is_odd(number):
    print(number)
    return False if number == 0 else is_even(number - 1)


def is_even(number):
    print(number)
    return True if number == 0 else is_odd(number - 1)

print(is_odd(21))
print(is_even(15))

