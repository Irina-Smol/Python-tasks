# Напишите программу, которая прочитает 3 числа и выведет максимум из них троих.
#Sample Input:
#8
#11
#9
#Sample Output:
#11

number_1, number_2, number_3 = int(input()), int(input()), int(input())

if number_2 > number_1:
    print(number_2)

elif number_3 > number_1:
    print(number_3)

else:
    print(number_1)
