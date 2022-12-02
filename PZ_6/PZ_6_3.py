import random  # Подключение модуля случайных значений
list = [] 
try:
    N = int(input("Длина списка: "))  # Длина списка
    for i in range(N):
        list.append(random.randint(0, 100))  # Заносим в пустой список рандомные числа от 0 до 100
    print(list)
    k = int(input('k = '))  # Сколько будет сдвигов
    k = min(k, len(list))
    list = [0]*k + list[:-k]  # Сдвигает индексы списка вправо
    print(list)
except ValueError:  # Если будет введено недопустимое значение
    print("Введено недопустимое значение")