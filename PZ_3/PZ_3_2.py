while True:
    znak = input("Знаки (+, -, /, *): ")  # Ввод арифметической операции на выбор
    if znak == "Стоп":  # Прерывания цикла с помощью слова "Стоп"
        break
    if znak in ('+', '-', '*', '/'):  # Условие
        x = float(input("x= "))
        y = float(input("y= "))
        if znak == '+':
            print(x + y)
        elif znak == '-':
            print(x - y)
        elif znak == '*':
            print(x * y)
        elif znak == "/":  # Обработка исключения (Деление на ноль)
            try:
                print(x / y)
            except ZeroDivisionError:
                print("Деление на 0!")
    else:  # Если пользователь ввёл недопустимый знак или значение
        print("Неверный знак операции!")
