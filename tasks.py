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

# 1.12.6
'''
n = int(input())
body = 'программистов'
if n == 1 or (n % 10 == 1 and n != 11 and n % 100 != 11):
    body = 'программист'
elif n in (2, 3, 4) or (n % 10 in (2, 3, 4) and n not in (12, 13, 14) and n % 100 not in (12, 13, 14)):
    body = 'программиста'
print(n, body)
'''

# 1.12.7
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
#################
'''
Напишите программу, которая подключает модуль math и, используя значение числа π \pi π из этого модуля, 
находит для переданного ей на стандартный ввод радиуса круга периметр этого круга и выводит его на стандартный вывод.

import math

r = float(input())

print(2 * math.pi * r)
'''
#################
'''
Напишите программу, которая запускается из консоли и печатает значения всех переданных аргументов на 
экран (имя скрипта выводить не нужно). Не изменяйте порядок аргументов при выводе.

Для доступа к аргументам командной строки программы подключите модуль sys и используйте переменную argv из этого модуля.

Пример работы программы:

> python3 my_solution.py arg1 arg2
arg1 arg2

import sys

counter = 1
while counter < len(sys.argv):
    print(sys.argv[counter], end=' ')
    counter += 1
'''
#################
'''
Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и посчитать число строк в нём.
Используйте функцию get для получения файла (имеет смысл вызвать метод strip к передаваемому параметру, чтобы убрать 
пробельные символы по краям).
После получения файла вы можете проверить результат, обратившись к полю text. Если результат работы скрипта не принимается, 
проверьте поле url на правильность. Для подсчёта количества строк разбейте текст с помощью метода splitlines.
В поле ответа введите одно число или отправьте файл, содержащий одно число.


import os
import requests

pathToFileIn = os.path.join('E:\Others', 'dataset_3378_2.txt')  # формируем путь к файлу
with open(pathToFileIn) as inf:
    url = inf.readline().strip()
#print(url)
file = requests.get(url)  #здесь мы получаем объект <class 'requests.models.Response'>
#print(file.text) #выведет текст в файле
#print(file.text.splitlines()) #весь текст в файле в список. в качестве элемента списка строка
print(len(file.text.splitlines()))
'''
#################
'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое последнего файла из набора, как ответ на это задание.

Задание написано не изменяя традициям... Для тех кто тупит в самом начале, но не хочет спойлеров разъясняю задание: 

Надо скачать файл из поля для решения, там будет ссылка, по ссылке файл с названием следующего документа внутри. 
Чтобы получить очередной документ, допишите его название к "https://stepic.org/media/attachments/course67/3.6.3/" . 
И так пока не упретесь в последний файл, там текст, начинается с "We",  его надо написать как ответ.

import os
import requests

pathToFileIn = os.path.join('E:\Others', 'dataset_3378_3(1).txt')  # формируем путь к файлу
with open(pathToFileIn) as inf:
    url = inf.readline().strip()
file = requests.get(url)  #здесь мы получаем объект <class 'requests.models.Response'>
res = ''
while True:
    tmp = file.text
    print(tmp[:2])
    if tmp[:2] != 'We':
        print(tmp)
        url = 'https://stepic.org/media/attachments/course67/3.6.3/' + file.text
        file = requests.get(url)
    else:
        res = tmp
        break
print(res)
'''
#################
'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча 
и выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число n n n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.

Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15


Sample Output:
Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6


n = int(input())
counter = 0

arr = []
while counter < n:
    arr += [input().split(';')]
    counter += 1
#print(arr)
s = dict()
counter = 0
for i in arr:
    team_1 = i[0]
    team_2 = i[2]
    if team_1 not in s:
        s.update({team_1: [1, 0, 0, 0, 0]})
    else:
        s[team_1][0] += 1

    if int(i[1]) > int(i[3]):
        s[team_1][1] += 1
    elif int(i[1]) == int(i[3]):
        s[team_1][2] += 1
    else:
        s[team_1][3] += 1

    if team_2 not in s:
        s.update({team_2: [1, 0, 0, 0, 0]})
    else:
        s[team_2][0] += 1

    if int(i[1]) < int(i[3]):
        s[team_2][1] += 1
    elif int(i[1]) == int(i[3]):
        s[team_2][2] += 1
    else:
        s[team_2][3] += 1

    counter += 1
for ind, val in s.items():
    s[ind][4] = val[1] * 3 + val[2]
    print(ind + ':' + str(val[0]) + ' ' + str(val[1]) + ' ' + str(val[2]) + ' ' + str(val[3]) + ' ' + str(val[4]))
#print(s)
'''
#################
'''
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
Попробуем написать подобную систему.
На вход программе первой строкой передаётся количество d известных нам слов, после чего на d 
строках указываются эти слова. Затем передаётся количество l строк текста для проверки, после чего l строк текста.
Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:
stepic
champignons
the
'''
n = int(input())
counter = 0
s = set()
while counter < n:
    s.add(input().lower())
    counter += 1
counter = 0
n = int(input())
arr = []
while counter < n:
    arr += [input().lower().split(' ')]
    counter += 1
s1 = set()
for i in arr:
    for j in i:
        s1.add(j)
res = set()

for x in s1:
    if x not in s:
            res.add(x)

for a in res:
    print(a)