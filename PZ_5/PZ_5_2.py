try:  # Обработка исключений
    def invertdigits(k):  # Переворачивает строку
        return int(str(k)[::-1])


    for i in range(0, 5):  # Повторение (5 раз)
        print('Введите число k: ')
        K = int(input())
        print('Обратный порядок цифр: ', invertdigits(K))

except ValueError:
    print("Вы ввели недопустимое значение")  # Если пользователь ввёл недопустимое значение
