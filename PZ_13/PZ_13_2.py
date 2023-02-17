"""Сгенерировать матрицу, в которой элементы больше 10  заменяются на 0."""

import random  # Добавляем библеотеку рандома

M = int(input("Количесвто столбцов: "))
N = int(input("Количество строк: "))
matrix = [[random.randrange(0, 20) for y in range(M)] for x in range(N)]  # Создание матрицы
c = [matrix[i] for i in range(N)]  # Преобразование матрицы в более понятный аид

print('Исходная матрица:')  # Вывод матрицы
for i in range(3):
    print(c[i])

print("Измененная матрица:")  # Вывод матрицы с условием, что значения, которые больше 10, заменяются на 0.
for i in range(M):
    for j in range(N):
        if matrix[i][j] > 10:
            matrix[i][j] = 0

print(f'{matrix[0]}\n'
      f'{matrix[1]}\n'
      f'{matrix[2]}\n')
