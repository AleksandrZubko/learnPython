# 1.12.1
'''
import math

a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c)) #квадратный корень
print(s)
'''

'''
#1.12.2
# (−15,12]∪(14,17)∪[19,+∞)
i = int(input())
if (i > -15 and i <= 12) or (i > 14 and i < 17) or (i >= 19):
    print(True)
else:
    print(False)
'''

# 1.12.3
'''
Напишите простой калькулятор, который считывает с пользовательского ввода три строки: 
первое число, второе число и операцию, после чего применяет операцию к введённым числам 
("первое число" "операция" "второе число") и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.

a = float(input())
b = float(input())
operation = input()
if operation == 'mod':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a % b)
elif operation == 'pow':
    print(a ** b)
elif operation == 'div':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a // b)
elif operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '/':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a / b)
elif operation == '*':
    print(a * b)
'''

# 1.12.4
'''
Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты бывают треугольные, прямоугольные и круглые. Чтобы быстро вычислять жилплощадь, требуется написать программу, на вход которой подаётся тип фигуры комнаты и соответствующие параметры, которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.

import math

figure = input()
if figure == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(s)
if figure == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a * b)
if figure == 'круг':
    r = int(input())
    print(3.14 * (r ** 2))
'''

# 1.12.5
'''
Напишите программу, которая получает на вход три целых числа, 
по одному числу в строке, и выводит на консоль в три строки сначала максимальное, 
потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.

a = int(input())
b = int(input())
c = int(input())

x1 = a
x2 = b
x3 = c

if b > a and b > c:
    x1 = b
    if a > c:
        x2 = a
    else:
        x2 = c
        x3 = a
elif c > a and c > b:
    x1 = c
    if a > b:
        x2 = a
        x3 = b
    else:
        x3 = a
elif c > b:
    x2 = c
    x3 = b
print(str(x1) + '\n' + str(x3) + '\n' + str(x2))
'''

#1.12.6
'''
n = int(input())
body = 'программистов'
if n == 1 or (n % 10 == 1 and n != 11 and n % 100 != 11):
    body = 'программист'
elif n in (2, 3, 4) or (n % 10 in (2, 3, 4) and n not in (12, 13, 14) and n % 100 not in (12, 13, 14)):
    body = 'программиста'
print(n, body)
'''

#1.12.7
'''

number_str = input()
first_part = number_str[:3] #3 символа слева
second_part = number_str[3:] #3 символа справа
s1 = 0
s2 = 0
for i in first_part: #пройтись циклом по строке
    s1 += int(i)
for i in second_part:
    s2 += int(i)
if s1 == s2:
    print('Счастливый')
else:
    print('Обычный')
'''

#################
'''
Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор, пока сумма введённых чисел 
не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0, после этого считывание продолжать не нужно.
В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что сумма этих чисел равна нулю и выводим 
сумму их квадратов, не обращая внимания на то, что остались ещё не прочитанные значения.

sumAll = 0
sumQ = 0
while True:
    i = int(input())
    sumAll += i
    sumQ += i**2
    if sumAll == 0:
        break
print(sumQ)
'''
#################
'''
Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... 
(число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число n — столько элементов 
последовательности должна отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел в одну строку.

Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

n = int(input())
res = []
tmp = []
cnt = 1
num = 1
while cnt <= n:
    tmp = [num]
    res += tmp * num
    cnt = len(res)
    num += 1

i = 0
while i < n:
    print(res[i], end=' ')
    i += 1
'''



