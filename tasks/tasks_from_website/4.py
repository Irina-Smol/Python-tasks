# слияние нескольких словарей в один

dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}

result = {}
for d in (dict_a, dict_b, dict_c):
    result.update(d)
print(result)


# 2) https://tproger.ru/translations/asterisks-in-python-what-they-are-and-how-to-use-them/
result2 = {**dict_a, **dict_b, **dict_c}
print(result2)

