""" Решето Эратосфена """

n = 10

a = [True] * n
a[0] = a[1] = False

for i in range(2, n):
    if a[i]:
        for m in range(2 * i, n, i):
            a[m] = False

for i in range(n):
    print(i, '-', 'простое' if a[i] else 'составное')