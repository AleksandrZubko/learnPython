'''
На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление исходной строки обратно.
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
и производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
Sample Input:
a3b4c2e10b1
Sample Output:
aaabbbbcceeeeeeeeeeb

import os

pathToFileIn = os.path.join('E:\Others', 'dataset_3363_2.txt')  #формируем путь к файлу
with open(pathToFileIn) as inf:
    stroka = inf.readline()
tmp = ''
num = '0'
res = ''
for s in stroka:
    if s.isalpha():
        res += tmp * int(num)
        num = '0'
        tmp = s
    else:
        num += s
res += tmp * int(num)

pathToFileOut = os.path.join('E:\Others', 'forTestRes.txt')
with open(pathToFileOut, 'w') as ouf:
    ouf.write(res )
'''
#################
'''
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое 
слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически 
первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.
Слова, написанные в разных регистрах, считаются одинаковыми.
Sample Input:
abc a bCd bC AbC BC BCD bcd ABC
Sample Output:
abc 3

import os

pathToFileIn = os.path.join('E:\Others', 'dataset_3363_3.txt')  # формируем путь к файлу
with open(pathToFileIn) as inf:
    stroka = inf.read().lower()
#print(stroka)
tmp = ''
dict = {}
for s in stroka:
    if s in (' ', '\n'):
        if tmp in dict:
            dict.update({tmp: dict[tmp] + 1})
        else:
            dict.update({tmp: 1})
        tmp = ''
    else:
        tmp += s

print(dict)
res = 'z'
maxCount = 0

for key, val in dict.items():
    if val >= maxCount and key < res:
        maxCount = val
        res = key

print(res, maxCount)
'''
#################
'''
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает его 
среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.
Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте полученные значения, 
разделённые пробелом, последней строкой в файл с ответом.
В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной строкой со средними 
оценками по трём предметам.
Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
 Sample Input:

Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85

Sample Output:

85.0
94.0
71.666666667
81.0 84.0 85.666666667
'''

import os

pathToFileIn = os.path.join('E:\Others', 'dataset_3363_4.txt')

arr = []
res = []
with open(pathToFileIn, encoding='utf-8') as inf:
    for i in inf:
        #print(i.strip().split(';'))
        arr += [i.strip().split(';')]
#print(len(arr))
#print(arr)

res = ''
m = 0
f = 0
r = 0
for i in arr:
    #print(i)
    x1 = int(i[1])
    x2 = int(i[2])
    x3 = int(i[3])
    res += (str(round(((x1 + x2 + x3) / 3), 9)) + '\n')
    m += x1
    f += x2
    r += x3

res += str(round(m / len(arr), 9)) + ' ' + str(round(f / len(arr), 9)) + ' ' + str(round(r / len(arr), 9))
print(res)
pathToFileOut = os.path.join('E:\Others', 'forTestRes.txt')
with open(pathToFileOut, 'w') as ouf:
    ouf.write(res)


