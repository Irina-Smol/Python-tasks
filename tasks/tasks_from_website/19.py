# С помощью анонимной функции извлеките из списка числа, делимые на 15

nums = [45, 55, 60, 37, 100, 105, 220]
result = list(filter(lambda x: not x % 15, nums))