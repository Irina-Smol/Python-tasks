'''
Прочитайте три числа. Выведите их в порядке неубывания.
Sample Input:
8
11
7
Sample Output:
7
8
11
'''

res = [int(input()),int(input()),int(input())]
for i in sorted(res):
    print(i)
