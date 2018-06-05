""" Алгоритм Евклида""" # Рекурсия

def gcd(a,b):
    """ Алгоритм Евклида mod 1 """
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)

def gcd(a, b):
    """ Алгоритм Евклида mod 2 """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcd(a ,b):
    """ Алгоритм Евклида mod 3 """
    return a if b == 0 else gcd(b, a % b)