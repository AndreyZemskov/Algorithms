def factorize_number(x):
    """ Алгоритм факторизации - разложение числа на множители """
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1

factorize_number(x)
