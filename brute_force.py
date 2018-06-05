def is_simple_number(x):
    """ Определяет является ли число простым, если простое, то возвращает True, иначе Folse """
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            divisor += 1
            # print(divisor)
            return False
    return True

print(is_simple_number(x))