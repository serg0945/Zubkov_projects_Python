"""
Даны температуры за месяц март. Необходимо найти количество положительных и отрицательных значений температур в месяце,
самую низкую и самую высокую температуры, а также среднемесячное значение температуры.
"""
from random import randint
from functools import reduce


tempt = [(randint(-8, 20)) for i in range(31)]
plus_tempt = [i for i in tempt if i > 0]
minus_tempt = [i for i in tempt if i < 0]
mid_tempt = reduce(lambda x, y: x+y, tempt) / len(tempt)
print(f'Температура в марте: {tempt}')
print(f'Количество положительных значений температур в месяце: {len(plus_tempt)}')
print(f'Количество отрицательных значений температур в месяце: {len(minus_tempt)}')
print(f'Самая высокая температура в марте: {max(tempt)}')
print(f'Самая низкая температуSра в марте: {min(tempt)}')
print(f'Среднемесячное значение температуры: {round(mid_tempt, 2)}')

