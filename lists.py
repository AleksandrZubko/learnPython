
'''
a = [1, 2, 3]
b = a
# значения списка b?

a[1] = 10
# значения списка b?

b[0] = 20
# значения списка a?

a = [5, 6]
# значения списка b?
print(b)
'''

####################
'''
Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.
Используйте метод split строки. 

list = [int(i) for i in input().split()]
sum = 0
for i in list:
    sum += i
print(sum)
'''

####################
'''
Напишите программу, на вход которой подаётся список чисел одной строкой. 
Программа должна для каждого элемента этого списка вывести сумму двух его соседей. 
Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. 
Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
Если на вход пришло только одно число, надо вывести его же.
Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

list = [int(i) for i in input().split()]
listRes = []
counter = 0
for i in list:
    if len(list) == 1:
        listRes.insert(counter, i)
        break
    elif counter == 0:
        listRes.insert(counter, list[1] + list[len(list) - 1])
    elif counter == len(list) - 1:
        listRes.insert(counter, list[0] + list[len(list) - 2])
    else:
        listRes.insert(counter,list[counter - 1] + list[counter + 1])
    counter += 1
for i in listRes:
    print(i, end=' ')
'''
####################
'''
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, 
которые встречаются в нём более одного раза.
Для решения задачи может пригодиться метод sort списка.
Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

list = [int(i) for i in input().split()]
list.sort(reverse=True)
listRes = []

while len(list) > 0:
    counter = 0
    cnt = 1
    while len(list) > 0:
        if len(list) > 1:
            if list[0] == list[1] and len(list) > 1:
                cnt += 1
                counter += 1
                del list[0]
            elif cnt > 1:
                listRes.insert(0, list[0])
                counter = 0
                cnt = 1
                del list[0]
            else:
                counter = 0
                cnt = 1
                del list[0]
        elif len(list) == 1:
            if cnt > 1:
                listRes.insert(0, list[0])
                counter = 0
                cnt = 1
                del list[0]
            else:
                del list[0]
for i in listRes:
    print(i, end=' ')
'''
#################
'''
Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки, 
которая выводит все позиции, на которых встречается число x в переданном списке lst.
Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).
Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
'''
list = [int(i) for i in input().split()]
n = int(input())
cnt = 0
listRes = []
for i in list:
    if i == n:
        listRes.append(cnt)
    cnt += 1
if len(listRes) == 0:
    listRes.append('Отсутствует')
for i in listRes:
    print(i, end=' ')

