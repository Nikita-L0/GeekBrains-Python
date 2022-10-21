# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

dec = int(input("Введите десятичное число - "))
bits_num = 0
while dec >= (2**bits_num):
    bits_num += 1
bin_num = []
print (f'Десятичному числу {dec} соответствует двоичное число - ', end=' ')
for i in range(0, bits_num):
    if (dec - 2**(bits_num-1-i)) >= 0:
        bin_num.append(1)
        dec = dec - 2**(bits_num-1-i)
    else:
        bin_num.append(0)
    print(bin_num[i], end=' ')
