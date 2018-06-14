array = [1, 2, 3, 4, 5]

def check_sorted(A, ascending=True):
    """ Проверка отсортированности за O(len(A)) """
    flag = True
    s = 2 * int(ascending) - 1
    for i in range(0, len(Array) - 1):
        if s * A[i] > s * A[i + 1]:
            flag = False
            break
    print(flag)

check_sorted(array)