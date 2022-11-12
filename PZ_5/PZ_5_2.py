try:  # Обработка исключений
    count = 0


    def invertdigits(k):  # Переворачивает строку
        return int(str(k)[::-1])


    while count < 5:  # Повторение (5 раз)
        count += 1
        print('Введите число k: ')
        K = int(input())
        print('Обратный порядок цифр: ', invertdigits(K))

except ValueError:
    print("Вы ввели недопустимое значение")  # Если пользователь ввёл недопустимое значение
