'''
Классическая задача "Fizz Buzz".
Прочитайте число. Если число делится на 3 выведите "Fizz", если на 5 – "Buzz". Если число делится на 3 и на 5 одновременно, то – "Fizz Buzz". В противном случае выведите само число. 
Все слова выводятся без кавычек.
Sample Input:
3
Sample Output:
Fizz
'''
a = int(input())
if a % 3 == 0 and a % 5 == 0:
    print('Fizz Buzz')
elif a % 3 == 0:
    print('Fizz')
elif a % 5 == 0:
    print('Buzz')
else:
    print(a)
