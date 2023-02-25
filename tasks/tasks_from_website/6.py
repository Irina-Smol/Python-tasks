# Напишите код, который переводит целое число в строку, при том что его можно применить в любой системе счисления

print(int('ABC', 16))

str_a = '50'
b = 10
c = int(str_a) + b
print("The value of c = ", c)

#Преобразование string в int в списке
str_lst = ['1', '2', '3']
int_lst = [int(x) for x in str_lst]
print(int_lst)

#Преобразование string во float в списке
str_lst = ['10.505', '2.3', '3.99']
float_lst = [float(x) for x in str_lst]
print(float_lst)

# Преобразование строки с запятыми в число в Python
str_a = '5,123,000'
int_b = int(str_a.replace(',', ''))
print("The integer value", int_b) # Результат — целое значение


# Преобразование int в string
a_string = "str function for int to string"
a_num = 456
print(a_string + str(a_num))

