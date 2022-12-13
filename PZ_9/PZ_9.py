#  Если данные заранее известны:
dict1 = {"A1": "1", "A2": "11", "A3": "111"}
dict2 = {"B1": "2", "B2": "22", "B3": "222"}
dict3 = {"C1": "3", "C2": "33", "C3": "333"}
dict_sum = {}

#  Объединение всех словарей в единый словарь
dict_sum.update(dict1)
dict_sum.update(dict2)
dict_sum.update(dict3)
print(dict1)
print(dict2)
print(dict3)
print(dict_sum)


# Если данные вводятся пользователем:
dict1 = {}
dict2 = {}
dict3 = {}
dict_sum = {}
length = 3
for element in range(0, length):
    dict1[input("Ключ: ")] = input("Значение: ")

for element in range(0, length):
    dict2[input("Ключ: ")] = input("Значение: ")

for element in range(0, length):
    dict3[input("Ключ: ")] = input("Значение: ")

#  Вывод словарей по отдельности
print("Словарь первый:", dict1)
print("Второй словарь:", dict2)
print("Третий словарь:", dict3)

#  Объединение всех словарей в единый словарь
dict_sum.update(dict1)
dict_sum.update(dict2)
dict_sum.update(dict3)
print("Объединенный словарь:", dict_sum)
