'''
example_dic = {'a': [1, 'd'], 2: [2, 'we'], 3: 8}
print(example_dic)
'''
######################
'''
Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d и два числа: key и value.
Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2∗key. Если и ключа 2∗key нет, 
то нужно добавить ключ 2∗key в словарь и сопоставить ему список из переданного элемента [value] [value] [value].
Пример работы функции:
d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}



def update_dictionary(d, key, value):
    tmp = []
    tmp.append(value)
    list = []
    if key in d:
        list = d[key]
        d[key] = list + tmp
    elif d.get(2 * key) is not None:
        list = d.get(2 * key)
        d[2 * key] = list + tmp
    else:
        d[2 * key] = list + tmp
'''
######################
'''
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и 
вывести получившуюся статистику.
Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке 
число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз.

Sample Input 1:
a aa abC aa ac abc bcd a
Sample Output 1:
ac 1
a 2
abc 2
bcd 1
aa 2
'''

'''
list = [i for i in input().split()]


def counter_words(list):
    res = dict()
    for s in list:
        if s.lower() in res:
            res[s.lower()] += 1
        else:
            res.update({s.lower(): 1})
    return res


for key, val in counter_words(list).items():
    print(key, val)
'''
'''
s = input().lower().split()
for i in set(s):
    print(i, s.count(i))
'''


def f(x):
    return x ** 2

i = int(input())
counter = 0
s = dict()
res = []
while counter < i:
    d = int(input())
    tmp = 0
    if d in s:
        res.append(s[d])
    else:
        tmp = f(d)
        res.append(tmp)
        s[d] = tmp
    counter += 1


for j in res:
    print(j)