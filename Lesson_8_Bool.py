# На вход поступает целое число.
# Программа должна вывести True, если введенное значение является положительным числом,
# в противном случае - False.
# Сделать задачу необходимо без использования условного оператора.
# x = int(input())
# print(x > 0)

# На вход поступает целое число.
# Программа должна вывести True, если введенное значение является четным числом,
# в противном случае - False.
# Сделать задачу необходимо без использования условного оператора.
# x = int(input())
# print(x % 2 ==0)

# На вход поступает целое число.
# Программа должна вывести True, если введенное значение кратно 6
# (без остатка делится на 6), в противном случае - False
# Сделать задачу необходимо без использования условного оператора.
# x = int(input())
# print(x % 6 ==0)

# На вход поступает целое число.
# Программа должна вывести True, если введенное значение не делится на 9,
# в противном случае - False.
# Сделать задачу необходимо без использования условного оператора.
# x = int(input())
# print(x % 9 != 0)

# На вход поступает целое положительное число.
# Программа должна вывести True, если у введенного числа последняя цифра 2,
# в противном случае - False.
# Сделать задачу необходимо без использования условного оператора.
# x = int(input())
# print(x % 10 == 2)

# На вход поступают два целых число.
# Программа должна вывести True, если оба числа делятся на 7, в противном случае - False.
# Сделать задачу необходимо без использования условного оператора.
# x,z = map(int,input().split())
# print(x % 7 == 0 and z % 7 ==0)

# На вход поступают три целых числа - стороны треугольника.
# Необходимо вывести True, если данные стороны образуют правильный треугольник,
# в противном случае - False.
# Сделать задачу необходимо без использования условного оператора.
# x, z, w = map(int, input().split())
# print(z == z == w)

# На вход поступает целое число.
# Программа должна вывести True, если введенное значение принадлежит интервалу от 5 не
# включительно до 19 включительно , в противном случае - False.
# Сделать задачу необходимо без использования условного оператора.
# a = int(input())
# print(a > 5 and a <= 19)

# На вход поступают два слова.
# Программа должна вывести True, если хотя бы одно слово равно слову "awesome".
# Сделать задачу необходимо без использования условного оператора.
# print('Введите два слова')
# a = input()
# b = input()
# c = 'awesome'
# print(a == c or b == c)

# На вход поступают три целых числа - стороны треугольника.
# Необходимо вывести True, если данные стороны образуют равнобедренный треугольник,
# в противном случае - False.
# Сделать задачу необходимо без использования условного оператора.
# x, z, w = map(int, input().split())
# print(x == z or x == w or z == w)

# На вход поступает целое положительное число.
# Программа должна вывести True, если данное число является двузначным, в противном случае - False.
# Сделать задачу необходимо без использования условного оператора.
# a = int(input())
# print(a >= 10 and a <= 99)
# print(10 <= a <= 99)

# На вход поступают три целых числа - стороны треугольника.
# Необходимо вывести True, если данные стороны образуют прямоугольный треугольник,
# в противном случае - False.
# Для написания программы необходимо вспомнить теорему Пифагора
# Сделать задачу необходимо без использования условного оператора.
x, z, w = map(int, input().split())
print(x ** 2 + z ** 2 == w ** 2 or x ** 2 + w ** 2 == z ** 2 or w ** 2 + z ** 2 == x ** 2)