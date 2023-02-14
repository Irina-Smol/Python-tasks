'''
Напишите программу, которая считывает координаты двух точек и определяет лежат ли эти точки в одной координатной четверти.
В качестве результата выведите "YES" или "NO" (заглавными буквами, без кавычек).
Sample Input:
1
2
3
4.1
Sample Output:
YES
'''
a1, b1, a2, b2 = float(input()), float(input()), float(input()), float(input())
if a1 * a2 > 0 and b1 * b2 > 0:
    print('YES')
else:
    print('NO')
