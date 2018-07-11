""" Копирование массива """

N = int(input('Введите размер массива: ')) # Размер массива
A = [0] * N
B = [0] * N
print(N)

for i in range(N):
    A[i] = int(input('Введите значения для массива: '))
    print('Переменная A равна {}'.format(A))
for i in range(N):
    B[i] = A[i]
    print('Переменная B равна {}'.format(B))

C = list(A) # Создаст новый список, копию списка A

def array_search(a:list, n:int, x:int): # a - массив, размер массива(диапазон поиска), x - искомое число
    """
        Линейный поиск в массиве
        осуществляет поиск числа x в массиве a
        от 0 до N-1 индекса включительно.
        Возвращает индекс элемента x в массиве а.
        Или -1, если такого нет.
        Если в массиве несколько одинковых элементов,
        равных x, то вернуть индекс первог опо счету.
    """
    for i in range(n):
        if a[i] == x:
            return i

    return 0

def test_array_search():
    a1 = [1, 2, 3, 4, 5]
    m = array_search(a1, 5, 8)
    if m == -1:
        print('test1 - OK')
    else:
        print('test1 - faile')

    a2 = [-1, -2, -3, -4, -5]
    m = array_search(a2, 5, -3)
    if m == 2:
        print('test2 - OK')
    else:
        print('test2 - faile')

    a3 = [10, 20, 30, 10, 10]
    m = array_search(a3, 5, 10)
    if m == 0:
        print('test3 - OK')
    else:
        print('test3 - faile')

test_array_search()

# Инверсия массива

def invert_array(a:list, n:int):
    """
       Инверсия массива
       в рамках от 0 до n-1
    """
    for i in range(n//2):
        a[i], a[n -1 -i] = a[n -1 -i], a[i]

def test_invert_array():
    a1 = [1, 2, 3, 4, 5]
    print(a1)
    invert_array(a1, 5)
    print(a1)
    if a1 == [5, 4, 3, 2, 1]:
        print('test1 - OK')
    else:
        print('test1 - faile')

    a2 = [0, 0, 0, 0, 0, 0, 0, 10]
    print(a2)
    invert_array(a2, 8)
    print(a2)
    if a2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print('test2 - OK')
    else:
        print('test2 - faile')

test_invert_array()
