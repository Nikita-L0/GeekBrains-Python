# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

N = int(input("Введите число N: "))
list_sum = [1]
for N in range(1, N+1):
    float: list_sum.append (round ((1+(1/N))**N, 2))
list_sum.remove(1)
print (f"Для N = {N} : [", end = "")
for i in range (1, N):
    print (f'{i}:{list_sum[i-1]}', end = ', ')
print (f'{N}:{list_sum[N-1]}]')
sum = 0
for i in range (N):
    sum += list_sum[i]
print(f'Сумма элементов равна {round(sum,2)}')