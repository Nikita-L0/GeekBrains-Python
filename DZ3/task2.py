# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

a = list(map(int, input('Введите список чисел через пробел: ').split()))
b = []
if len(a) % 2 == 0:
    i = 0
    while i < len(a)/2:
        b.append(a[i] * a [-(i+1)])
        i += 1
else:
    i = 0
    while i < len(a)/2:
        b.append(a[i] * a [-(i+1)])
        i += 1
print (b)