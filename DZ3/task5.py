# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
#  для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число - '))

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
fib = []
for i in range (0, k):
    fib.append(fibonacci (i+1))

def nfibonacci(n):
    def fibonacci(n):
        if n in (1, 2):
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    if n in (-1, -2, -1):
        return 1, -1
    return ((-1)**(n+1)) * fibonacci (n)
nfib = []
for i in range (0, k):
    nfib.append(nfibonacci (i+1))
nfib.reverse()
nfib.append (0)
nfib.extend (fib)
print (f'Последовательность Фибоначчи для числа {k}, в том числе с отрицательными значениями равна {nfib}')
