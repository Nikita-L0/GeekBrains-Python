A = list(map(int, input('Введите координаты X и Y первой точки через пробел: ').split()))
B = list(map(int, input('Введите координаты X и Y первой точки через пробел: ').split()))
C = ((A[0]-B[0])**2 + (A[1]-B[1])**2)**(0.5)
print(f'Расстояние между точками с координатами ({A[0]}, {A[1]}) и ({B[0]}, {B[1]}) равно {round(C, 5)}')