A, B, C = input("Введите первое число: "), input("Введите второе число: "), input("Введите третье число: ")
# Ввод значений пользователем

while (type(A) != int) & (type(B) != int) & (type(C) != int):  # Обработка исключений
    try:
        A = int(A)
        B = int(B)
        C = int(C)

        if (B > A) and (C > B):  # Условие
            print("Данное высказывание (A<B<C) истинно")
        else:
            print("Данное высказывание (A<B<C) неистинно")
    except ValueError:  # Если пользователь ввёл недопустимое значение
        print("Вы ввели недопустимое значение")
