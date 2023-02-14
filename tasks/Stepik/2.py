# Напишите программу, которая будет получать на вход количество,  
# а выводить это число и правильное склонение слова "студент" латиницей ("student", "studenta", "studentov").
# Между числом и словом должен быть ровно один пробел.

#Sample Input:
#3
#Sample Output:
#3 studenta

n = input()

if n[-2:] in ('11', '12', '13', '14'):
    print(n, 'studentov')
elif n[-1] == '1':
    print(n, 'student')
elif n[-1] in ('2', '3', '4'):
    print(n, 'studenta')
else:
    print(n, 'studentov')
