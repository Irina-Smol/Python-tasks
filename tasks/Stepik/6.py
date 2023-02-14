'''
Выведите цвет клетки доски по её координатам.
Координаты клетки заданы двумя числами от 1 до 8. Сначала номер столбца, потом номер строки.
В качестве ответа выведите "BLACK" или "WHITE" без кавычек.
Sample Input:
1
1
Sample Output:
BLACK
'''
x , y = int(input()), int(input())
if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
    print('BLACK')
else:
    print('WHITE')
