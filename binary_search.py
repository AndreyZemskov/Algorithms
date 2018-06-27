def binary_search(A, key): # скорость поиска O(log2N)
    left = 0
    right = len(A)
    while left < right:
        middle = (left + right) // 2
        if key > A[middle]:
            left = middle + 1
        else:
            right = middle
    if left != len(A) and A[left] == key:
        return left
    else:
        print('{} is not in sequence'.format(key))
