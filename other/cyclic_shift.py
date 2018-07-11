"""Сдвиг влево """

a = [1, 2, 3, 4, 5]
tmp = a[0]
for i in range(a[4] - 1):
    a[i] = a[i + 1]
a[a[4] - 1] = tmp

print(a)

"""Сдвиг вправо """

a = [1, 2, 3, 4, 5]
tmp = a[4]
for i in range(a[4] - 2, -1, -1):
    a[i + 1] = a[i]
a[0] = tmp

print(a)