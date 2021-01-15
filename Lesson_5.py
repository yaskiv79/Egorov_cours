a = input()
print(type(a))
a = int(input())
print(type(a))
a = input()
print(type(a))
a = int(a)
print(type(a))
c = int(input())
print(type(c))
d = float(input())
print(type(d), d)
print('Вычислим периметр треугольника')
a = float(input('введите значение а: '))
b = float(input('введите значение b: '))
c = float(input('введите значение c: '))
print('Стороны треугольника:', a, b, c)
d = a + b + c
print('Периметр равен', d)
print('А теперь введите все три значения через пробел: ')
a, b, c = map(int, input() .split())
d = a + b + c
print('Периметр равен', d)




