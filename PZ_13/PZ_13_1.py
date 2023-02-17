"""В матрице элементы первого столбца возвести в куб."""

import random  # Добавляем библеотеку рандома

M = int(input("Количесвто столбцов: "))
N = int(input("Количество строк: "))
matrix = [[random.randrange(0, 10) for y in range(M)] for x in range(N)]  # Создание матрицы
c = [matrix[i] for i in range(N)]  # Преобразование матрицы в более понятный аид

print('Исходная матрица:')  # Вывод матрицы
for i in range(3):
    print(c[i])

print("Измененная матрица:")  # Вывод матрицы с измененным первым столбцом
for i in range(0, len(matrix)):
    matrix[i][0] = matrix[i][0] ** 3  # Изменение первого столбца

print(f'{matrix[0]}\n'
      f'{matrix[1]}\n'
      f'{matrix[2]}\n')
