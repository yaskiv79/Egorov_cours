# Напишите программу, которая вычисляет длину отрезка (т.е. расстояние между двумя
# точками), заданного двумя значениями x1 и x2 (вещественные числа).
# Sample Input 1: -2 6.5 Sample Output 1: 8.5
# Sample Input 2: 3 -9 Sample Output 2: 12.0
# Sample Input 3: 5 3 Sample Output 3: 2.0
x1, x2 = map(float, input() .split())
a = max(x1, x2)
b = min(x1, x2)
d = a - b
print(d)


