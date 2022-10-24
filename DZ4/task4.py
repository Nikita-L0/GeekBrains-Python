# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите число k = '))
print(f'Многочлен со старшей степенью равной {k} - {random.randint(1,100)}x**{k} +', end=' ')
m = k-1
while m !=1:
    c = random.randint(0,100)
    if c!=0:
        print(f'{c}x**({m}) +', end=' ')
    else:
        {}
    m -= 1
c = random.randint(0,100)
if c!=0:
        print(f'{c}x +', end=' ')
c = random.randint(0,100)
if c!=0:
        print(f'{c} = 0')


