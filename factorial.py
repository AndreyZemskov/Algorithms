""" Факториал """ # Рекурсия

def factorial(n):
    assert n >= 0, 'Факториал отрицательного не определен'
    if n == 0:
        return 1
    return factorial(n - 1) * n

print(factorial(5))