try:  # Обработка исключений
    Sm = int(input('Введите требуемую длину в сантиметрах : '))
    Metr = Sm // 100
    if Metr == 0:
        print('Вводимое число меньше одного полного метра')
    else:
        print(Metr)
except ValueError:  # Если пользователь ввёл другой тип (не int)
    print("Произошла ошибка, потому что вы ввели не число!")
