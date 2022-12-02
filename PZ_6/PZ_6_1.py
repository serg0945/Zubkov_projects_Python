list1 = []
try:
    a = int(input("Введите число A: "))  # Запись значений для первых двух чисел
    b = int(input("Введите число B: "))
    summ = a + b
    list1.append(a)
    list1.append(b)  # Заносим в пустой список наши первые два числа
    for count in range(2, 10):  # Диапозон от 3 числа до 10 числа
        list1.append(summ)
        list1[count] = summ
        summ += list1[count]  # Каждое последующее число будет равно сумме предыдущих
    print(list1)
except ValueError:  # Если будет введено недопустимое значение
    print("Введено недопустипое значение")

