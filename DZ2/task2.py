# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input("Введите число N: "))
list_sum = [1]
for N in range(1, N+1):
    list_sum.append (N*list_sum[N-1])
list_sum.remove(1)
print (f"Произведение чисел от 1 до {N} = {list_sum}")