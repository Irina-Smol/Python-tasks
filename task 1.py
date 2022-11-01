size = int(input())   # размер массива
array = []

for element in range(size):
    value = list(map(int, input().split()))  # написание чисел через пробел
    array.append(value)   # сохранение чисел в массиве

# for element in array:   # в результате ввода -> матрица
    # print(element)

for column in range(size-1, -1, -1):
    for row in range(size - 1, -1, -1):
        #print(row, column, array[row][column]) # показывает сначала ряд, затем колонну числа,
                                               # потом само число по данному ряду и колонне
        print(array[row][column], end=' ')
    print()